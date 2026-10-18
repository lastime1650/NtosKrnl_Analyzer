# ViIrqlLogCRStackTrace

- RVA: `0x00BAD6E8`–`0x00BAD75B` (길이 `115` bytes)
- VA: `0x0000000140BAD6E8`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `30`개 명령, `115/115` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00BAD73C` → [RtlCaptureStackBackTrace](../../text/2F/RtlCaptureStackBackTrace_function_002F9FF0.md) (function, `0x002F9FF0`)

### Direct callers
- [ViIrqlKeEnterCriticalRegion_Exit](ViIrqlKeEnterCriticalRegion_Exit_function_00BAD670.md) at `0x00BAD674`
- [ViIrqlKeLeaveCriticalRegion_Entry](ViIrqlKeLeaveCriticalRegion_Entry_function_00BAD690.md) at `0x00BAD699`

### Static image references
- `0x00BAD6F2` → RVA `0x00FFDA60` (`PAGEVRFD`; read)
- `0x00BAD701` → RVA `0x00FFDB7C` (`PAGEVRFD`; read/write)
- `0x00BAD709` → RVA `0x00FF4018` (`PAGEVRFD`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BAD73C` → [RtlCaptureStackBackTrace](../../text/2F/RtlCaptureStackBackTrace_function_002F9FF0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BAD6E8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00BAD6ED  57                              push rdi
00BAD6EE  48 83 EC 20                     sub rsp, 0x20
00BAD6F2  48 83 3D 66 03 45 00 00         cmp qword ptr [rip + 0x450366], 0
00BAD6FA  74 53                           je 0x140bad74f
00BAD6FC  B8 01 00 00 00                  mov eax, 1
00BAD701  F0 0F C1 05 73 04 45 00         lock xadd dword ptr [rip + 0x450473], eax
00BAD709  8B 1D 09 69 44 00               mov ebx, dword ptr [rip + 0x446909]
00BAD70F  FF C0                           inc eax
00BAD711  FF CB                           dec ebx
00BAD713  45 33 C9                        xor r9d, r9d
00BAD716  48 23 D8                        and rbx, rax
00BAD719  33 C9                           xor ecx, ecx
00BAD71B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00BAD724  48 C1 E3 06                     shl rbx, 6
00BAD728  48 03 1D 31 03 45 00            add rbx, qword ptr [rip + 0x450331]
00BAD72F  41 8D 79 07                     lea edi, [r9 + 7]
00BAD733  8B D7                           mov edx, edi
00BAD735  4C 8D 43 08                     lea r8, [rbx + 8]
00BAD739  48 89 03                        mov qword ptr [rbx], rax
00BAD73C  E8 AF C8 74 FF                  call 0x1402f9ff0
00BAD741  66 3B C7                        cmp ax, di
00BAD744  73 09                           jae 0x140bad74f
00BAD746  0F B7 C0                        movzx eax, ax
00BAD749  48 83 64 C3 08 00               and qword ptr [rbx + rax*8 + 8], 0
00BAD74F  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00BAD754  48 83 C4 20                     add rsp, 0x20
00BAD758  5F                              pop rdi
00BAD759  C3                              ret
00BAD75A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViIrqlLogCRStackTrace(int a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if ((*(unsigned __int64 *)(v_rip + 4522854)) == 0) goto loc_00BAD74F;
    result = (unsigned int)((1) + 1);
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 4483337))) - 1);
    a4 = 0;
    v_rbx = (v_rbx) & (result);
    a1 = 0;
    v_rbx = (v_rbx) << (6);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_rip + 4522801));
    *(unsigned __int64 *)(v_rbx) = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = RtlCaptureStackBackTrace(a1, (unsigned int)((unsigned int)(a4 + 7)), v_rbx + 8, a4);
    if (((unsigned __int16)(result)) < ((unsigned __int16)(a4 + 7))) {
        result = (unsigned __int16)(result);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViIrqlLogCRStackTrace(int32_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if ((*(uint64_t *)(v_rip + 0x450366)) == 0) goto loc_00BAD74F;
    result = (uint32_t)((1) + 1);
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x446909))) - 1);
    Arg4 = 0;
    local_rbx = (local_rbx) & (result);
    Arg1 = 0;
    local_rbx = (local_rbx) << (6);
    local_rbx = (local_rbx) + (*(uint64_t *)(v_rip + 0x450331));
    *(uint64_t *)(local_rbx) = *(uint64_t *)(gs_base + (0 + 0x188));
    result = RtlCaptureStackBackTrace(Arg1, (uint32_t)((uint32_t)(Arg4 + 7)), local_rbx + 8, Arg4);
    if (((uint16_t)(result)) < ((uint16_t)(Arg4 + 7))) {
        result = (uint16_t)(result);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BAD6E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BAD6E8[BB_00BAD6E8]
  bb_00BAD6FC[BB_00BAD6FC]
  bb_00BAD746[BB_00BAD746]
  bb_00BAD74F[BB_00BAD74F]
  bb_00BAD75A[BB_00BAD75A]
  bb_00BAD6E8 -->|branch| bb_00BAD74F
  bb_00BAD6E8 -->|fallthrough| bb_00BAD6FC
  bb_00BAD6FC -->|branch| bb_00BAD74F
  bb_00BAD6FC -->|fallthrough| bb_00BAD746
  bb_00BAD746 -->|flow| bb_00BAD74F
```
