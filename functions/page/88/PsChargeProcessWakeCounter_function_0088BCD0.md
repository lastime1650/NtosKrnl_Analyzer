# PsChargeProcessWakeCounter

- RVA: `0x0088BCD0`–`0x0088BD37` (길이 `103` bytes)
- VA: `0x000000014088BCD0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007D3D8`
- 디코드: `28`개 명령, `103/103` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0088BCEF` → [PsGetProcessInheritedFromUniqueProcessId](../../text/45/PsGetProcessInheritedFromUniqueProcessId_function_0045D350.md) (function, `0x0045D350`)
- `0x0088BD1A` → [PspChargeProcessWakeCounter](PspChargeProcessWakeCounter_function_0088D2A0.md) (function, `0x0088D2A0`)

### Direct callers
- [EtwpQueueNotification](../8C/EtwpQueueNotification_function_008C870C.md) at `0x008C88D4`
- [PopPowerRequestSpecialRequestSet](../A2/PopPowerRequestSpecialRequestSet_function_00A21B4C.md) at `0x00A21BE5`
- [PspCreateActivityReference](../A8/PspCreateActivityReference_function_00A8F110.md) at `0x00A8F1CD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0088BCEF` → [PsGetProcessInheritedFromUniqueProcessId](../../text/45/PsGetProcessInheritedFromUniqueProcessId_function_0045D350.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0088BCD0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0088BCD5  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0088BCDA  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0088BCDF  57                              push rdi
0088BCE0  48 83 EC 40                     sub rsp, 0x40
0088BCE4  49 8B F9                        mov rdi, r9
0088BCE7  41 8B F0                        mov esi, r8d
0088BCEA  8B EA                           mov ebp, edx
0088BCEC  48 8B D9                        mov rbx, rcx
0088BCEF  E8 5C 16 BD FF                  call 0x14045d350
0088BCF4  48 85 C0                        test rax, rax
0088BCF7  74 3C                           je 0x14088bd35
0088BCF9  48 C7 44 24 30 00 00 00 00      mov qword ptr [rsp + 0x30], 0
0088BD02  4C 8B CF                        mov r9, rdi
0088BD05  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
0088BD0A  44 8B C6                        mov r8d, esi
0088BD0D  8B D5                           mov edx, ebp
0088BD0F  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
0088BD17  48 8B CB                        mov rcx, rbx
0088BD1A  E8 81 15 00 00                  call 0x14088d2a0
0088BD1F  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0088BD24  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0088BD29  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0088BD2E  48 83 C4 40                     add rsp, 0x40
0088BD32  5F                              pop rdi
0088BD33  C3                              ret
0088BD34  CC                              int3
0088BD35  EB E8                           jmp 0x14088bd1f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsChargeProcessWakeCounter(__int64 a1, int a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int8 v_stack_m20;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (64);
    result = PsGetProcessInheritedFromUniqueProcessId(a1, a2, a3, a4);
    if (result == 0) goto loc_0088BD35;
    v_stack_m18 = 0;
    v_stack_m20 = 1;
    v_stack_m28 = 1;
    result = PspChargeProcessWakeCounter(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
loc_0088BD1F:
    v_rsp = (v_rsp) + (64);
    return result;
loc_0088BD35:
    goto loc_0088BD1F;
}
```

## 5. (Beta) C Style

```c
int64_t PsChargeProcessWakeCounter(int64_t Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint8_t v_stack_m20;
    uint32_t v_stack_m28;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (64);
    result = PsGetProcessInheritedFromUniqueProcessId(Arg1, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0088BD35;
    v_stack_m18 = 0;
    v_stack_m20 = 1;
    v_stack_m28 = 1;
    result = PspChargeProcessWakeCounter(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
loc_0088BD1F:
    local_rsp = (local_rsp) + (64);
    return result;
loc_0088BD35:
    goto loc_0088BD1F;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0088BCD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0088BCD0[BB_0088BCD0]
  bb_0088BCF9[BB_0088BCF9]
  bb_0088BD1F[BB_0088BD1F]
  bb_0088BD34[BB_0088BD34]
  bb_0088BD35[BB_0088BD35]
  bb_0088BCD0 -->|branch| bb_0088BD35
  bb_0088BCD0 -->|fallthrough| bb_0088BCF9
  bb_0088BCF9 -->|flow| bb_0088BD1F
  bb_0088BD34 -->|flow| bb_0088BD35
  bb_0088BD35 -->|branch| bb_0088BD1F
```
