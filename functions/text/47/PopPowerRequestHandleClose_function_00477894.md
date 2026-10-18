# PopPowerRequestHandleClose

- RVA: `0x00477894`–`0x0047790E` (길이 `122` bytes)
- VA: `0x0000000140477894`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000ACCDC`
- 디코드: `34`개 명령, `122/122` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004778CC` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x004778DC` → [PopPowerRequestEvaluatePendingRequestStatus](PopPowerRequestEvaluatePendingRequestStatus_function_00477914.md) (function, `0x00477914`)
- `0x004778F0` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x004778FD` → [PopPowerRequestCallbackWorker](PopPowerRequestCallbackWorker_function_00477AD0.md) (function, `0x00477AD0`)

### Direct callers
- [PoDeletePowerRequest](../../page/A4/PoDeletePowerRequest_function_00A48F00.md) at `0x00A48F09`
- [PopPowerRequestClose](../../page/A9/PopPowerRequestClose_function_00A9D500.md) at `0x00A9D50D`

### Static image references
- `0x004778B9` → RVA `0x00F0ED30` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00477894  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00477899  55                              push rbp
0047789A  48 8B EC                        mov rbp, rsp
0047789D  48 83 EC 50                     sub rsp, 0x50
004778A1  33 C0                           xor eax, eax
004778A3  48 8D 55 E0                     lea rdx, [rbp - 0x20]
004778A7  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
004778AB  48 8B D9                        mov rbx, rcx
004778AE  48 8D 45 D0                     lea rax, [rbp - 0x30]
004778B2  0F 57 C0                        xorps xmm0, xmm0
004778B5  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
004778B9  48 8D 0D 70 74 A9 00            lea rcx, [rip + 0xa97470]
004778C0  48 8D 45 D0                     lea rax, [rbp - 0x30]
004778C4  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
004778C8  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
004778CC  E8 CF DE DF FF                  call 0x1402757a0
004778D1  48 8D 55 D0                     lea rdx, [rbp - 0x30]
004778D5  C6 43 20 01                     mov byte ptr [rbx + 0x20], 1
004778D9  48 8B CB                        mov rcx, rbx
004778DC  E8 33 00 00 00                  call 0x140477914
004778E1  48 8D 45 D0                     lea rax, [rbp - 0x30]
004778E5  48 39 45 D0                     cmp qword ptr [rbp - 0x30], rax
004778E9  48 8D 4D E0                     lea rcx, [rbp - 0x20]
004778ED  0F 95 C3                        setne bl
004778F0  E8 EB B3 EC FF                  call 0x140342ce0
004778F5  84 DB                           test bl, bl
004778F7  74 09                           je 0x140477902
004778F9  48 8D 4D D0                     lea rcx, [rbp - 0x30]
004778FD  E8 CE 01 00 00                  call 0x140477ad0
00477902  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00477907  48 83 C4 50                     add rsp, 0x50
0047790B  5D                              pop rbp
0047790C  C3                              ret
0047790D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPowerRequestHandleClose(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m18 = 0;
    v_stack_m30 = v_stack_m38;
    v_stack_m38 = v_stack_m38;
    v_stack_m28 = v_xmm0;
    result = KeAcquireInStackQueuedSpinLock(v_rip + 11105392, v_stack_m28, a3, a4);
    *(unsigned __int8 *)(a1 + 32) = 1;
    result = PopPowerRequestEvaluatePendingRequestStatus(a1, v_stack_m38, a3, a4);
    v_rbx = (v_stack_m38 != v_stack_m38) ? 1 : 0;
    result = KeReleaseInStackQueuedSpinLock(v_stack_m28, v_stack_m38, a3, a4);
    if ((unsigned __int8)(v_rbx) != 0) {
        a1 = v_stack_m38;
        result = PopPowerRequestCallbackWorker(a1, v_stack_m38, a3, a4);
    }
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopPowerRequestHandleClose(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m18 = 0;
    v_stack_m30 = v_stack_m38;
    v_stack_m38 = v_stack_m38;
    v_stack_m28 = v_xmm0;
    result = KeAcquireInStackQueuedSpinLock(v_rip + 11105392, v_stack_m28, a3, a4);
    *(uint8_t *)(arg1 + 0x20) = 1;
    result = PopPowerRequestEvaluatePendingRequestStatus(Arg1, v_stack_m38, a3, a4);
    local_rbx = (v_stack_m38 != v_stack_m38) ? 1 : 0;
    result = KeReleaseInStackQueuedSpinLock(v_stack_m28, v_stack_m38, a3, a4);
    if ((uint8_t)(local_rbx) != 0) {
        Arg1 = v_stack_m38;
        result = PopPowerRequestCallbackWorker(Arg1, v_stack_m38, a3, a4);
    }
    local_rsp = (local_rsp) + (80);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00477894&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00477894[BB_00477894]
  bb_004778F9[BB_004778F9]
  bb_00477902[BB_00477902]
  bb_0047790D[BB_0047790D]
  bb_00477894 -->|branch| bb_00477902
  bb_00477894 -->|fallthrough| bb_004778F9
  bb_004778F9 -->|flow| bb_00477902
```
