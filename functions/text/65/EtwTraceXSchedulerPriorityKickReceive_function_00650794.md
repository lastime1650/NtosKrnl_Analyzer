# EtwTraceXSchedulerPriorityKickReceive

- RVA: `0x00650794`–`0x00650802` (길이 `110` bytes)
- VA: `0x0000000140650794`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B3A94`
- 디코드: `23`개 명령, `110/110` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006507EA` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x006507F7` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KeSetThreadSchedulerAssist](../30/KeSetThreadSchedulerAssist_function_003038F8.md) at `0x00303B41`

### Static image references
- `0x00650798` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00650794  48 83 EC 58                     sub rsp, 0x58
00650798  48 8B 05 A1 9F 7B 00            mov rax, qword ptr [rip + 0x7b9fa1]
0065079F  48 33 C4                        xor rax, rsp
006507A2  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
006507A7  8B 81 10 05 00 00               mov eax, dword ptr [rcx + 0x510]
006507AD  41 B9 74 0F 00 00               mov r9d, 0xf74
006507B3  83 64 24 44 00                  and dword ptr [rsp + 0x44], 0
006507B8  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
006507BD  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
006507C1  41 B8 20 00 00 A0               mov r8d, 0xa0000020
006507C7  48 8D 44 24 30                  lea rax, [rsp + 0x30]
006507CC  89 54 24 34                     mov dword ptr [rsp + 0x34], edx
006507D0  BA 01 00 00 00                  mov edx, 1
006507D5  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
006507DA  C7 44 24 40 08 00 00 00         mov dword ptr [rsp + 0x40], 8
006507E2  C7 44 24 20 02 02 00 00         mov dword ptr [rsp + 0x20], 0x202
006507EA  E8 61 4B BE FF                  call 0x140235350
006507EF  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
006507F4  48 33 CC                        xor rcx, rsp
006507F7  E8 44 BE 05 00                  call 0x1406ac640
006507FC  48 83 C4 58                     add rsp, 0x58
00650800  C3                              ret
00650801  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTraceXSchedulerPriorityKickReceive(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m24;
    unsigned int v_stack_m28;
    unsigned int v_stack_m38;

    v_rsp = (v_rsp) - (88);
    result = (*(unsigned __int64 *)(v_rip + 8101793)) ^ (v_rsp);
    v_stack_m10 = result;
    v_stack_m28 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1296)));
    v_stack_m24 = a2;
    v_stack_m20 = v_stack_m28;
    v_stack_m18 = 8;
    v_stack_m38 = 514;
    result = EtwTraceKernelEvent(v_stack_m20, 1, (unsigned int)(0xA0000020ULL), (unsigned int)(0xF74ULL));
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, 1, (unsigned int)(0xA0000020ULL), (unsigned int)(0xF74ULL));
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwTraceXSchedulerPriorityKickReceive(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m24;
    uint32_t v_stack_m28;
    uint32_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    result = (*(uint64_t *)(v_rip + 0x7B9FA1)) ^ (local_rsp);
    v_stack_m10 = result;
    v_stack_m28 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x510)));
    v_stack_m24 = Arg2;
    v_stack_m20 = v_stack_m28;
    v_stack_m18 = 8;
    v_stack_m38 = 514;
    result = EtwTraceKernelEvent(v_stack_m20, 1, (uint32_t)(0xA0000020ULL), (uint32_t)(0xF74ULL));
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 1, (uint32_t)(0xA0000020ULL), (uint32_t)(0xF74ULL));
    local_rsp = (local_rsp) + (88);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x510` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00650794&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00650794[BB_00650794]
  bb_00650801[BB_00650801]
```
