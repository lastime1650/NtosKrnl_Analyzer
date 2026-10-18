# CmpDoQueueSystemHiveHysteresis

- RVA: `0x007E224C`–`0x007E229B` (길이 `79` bytes)
- VA: `0x00000001407E224C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `22`개 명령, `79/79` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x007E2262` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007E228D` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)

### Direct callers
- [CmRegisterSystemHiveLimitCallback](CmRegisterSystemHiveLimitCallback_function_007E213C.md) at `0x007E21B4`
- [CmpUpdateSystemHiveHysteresis](../A7/CmpUpdateSystemHiveHysteresis_function_00A720C4.md) at `0x00A72121`
- [sub_00B40366](../B4/Unknown_function_00B40366.md) at `0x00B40395`

### Static image references
- `0x007E2270` → RVA `0x007E23C0` (`CmpSystemHiveHysteresisWorker`; read)
- `0x007E2283` → RVA `0x00EEFBB0` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007E2262` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007E228D` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007E224C  40 53                           push rbx
007E224E  48 83 EC 20                     sub rsp, 0x20
007E2252  BA 20 00 00 00                  mov edx, 0x20
007E2257  8B D9                           mov ebx, ecx
007E2259  41 B8 43 4D 20 20               mov r8d, 0x20204d43
007E225F  8D 4A 20                        lea ecx, [rdx + 0x20]
007E2262  E8 89 FE 39 00                  call 0x140b820f0
007E2267  48 85 C0                        test rax, rax
007E226A  74 28                           je 0x1407e2294
007E226C  48 83 20 00                     and qword ptr [rax], 0
007E2270  48 8D 0D 49 01 00 00            lea rcx, [rip + 0x149]
007E2277  48 89 48 10                     mov qword ptr [rax + 0x10], rcx
007E227B  BA 01 00 00 00                  mov edx, 1
007E2280  48 8B C8                        mov rcx, rax
007E2283  89 1D 27 D9 70 00               mov dword ptr [rip + 0x70d927], ebx
007E2289  48 89 40 18                     mov qword ptr [rax + 0x18], rax
007E228D  E8 8E 72 B1 FF                  call 0x1402f9520
007E2292  B0 01                           mov al, 1
007E2294  48 83 C4 20                     add rsp, 0x20
007E2298  5B                              pop rbx
007E2299  C3                              ret
007E229A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpDoQueueSystemHiveHysteresis(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ExAllocatePool2(32 + 32, 32, (unsigned int)(0x20204D43ULL), a4);
    if (result != 0) {
        a1 = v_rip + 329;
        *(unsigned __int64 *)(result + 16) = a1;
        a2 = 1;
        a1 = result;
        *(unsigned int *)(v_rip + 7395623) = (unsigned int)((unsigned int)(a1));
        *(unsigned __int64 *)(result + 24) = result;
        result = ExQueueWorkItem(a1, a2, (unsigned int)(0x20204D43ULL), a4);
        result = 1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpDoQueueSystemHiveHysteresis(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ExAllocatePool2(32 + 32, 32, (uint32_t)(0x20204D43ULL), a4);
    if (result != 0) {
        Arg1 = v_rip + 329;
        *(uint64_t *)(result + 0x10) = Arg1;
        a2 = 1;
        Arg1 = result;
        *(uint32_t *)(v_rip + 0x70D927) = (uint32_t)((uint32_t)(Arg1));
        *(uint64_t *)(result + 0x18) = result;
        result = ExQueueWorkItem(Arg1, a2, (uint32_t)(0x20204D43ULL), a4);
        result = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007E224C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007E224C[BB_007E224C]
  bb_007E226C[BB_007E226C]
  bb_007E2294[BB_007E2294]
  bb_007E229A[BB_007E229A]
  bb_007E224C -->|branch| bb_007E2294
  bb_007E224C -->|fallthrough| bb_007E226C
  bb_007E226C -->|flow| bb_007E2294
```
