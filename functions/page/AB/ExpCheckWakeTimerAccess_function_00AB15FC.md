# ExpCheckWakeTimerAccess

- RVA: `0x00AB15FC`–`0x00AB16B7` (길이 `187` bytes)
- VA: `0x0000000140AB15FC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068F24`
- 디코드: `38`개 명령, `187/187` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00AB1637` → [SeCaptureSubjectContextEx](../8C/SeCaptureSubjectContextEx_function_008C4C90.md) (function, `0x008C4C90`)
- `0x00AB1691` → [SeAccessCheckWithHint](../../text/3A/SeAccessCheckWithHint_function_003A6C30.md) (function, `0x003A6C30`)
- `0x00AB169B` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)

### Direct callers
- [ExpSetTimerObject](../../text/23/ExpSetTimerObject_function_00231730.md) at `0x002323CB`
- [ExpCheckIRTimerAccess](../A2/ExpCheckIRTimerAccess_function_00A2C83C.md) at `0x00A2C8A4`

### Static image references
- `0x00AB163C` → RVA `0x00FC6D98` (`ALMOSTRO`; read)
- `0x00AB166E` → RVA `0x00B4F050` (`ExpWakeTimerSecurityDescriptor`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00AB1691` → [SeAccessCheckWithHint](../../text/3A/SeAccessCheckWithHint_function_003A6C30.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB15FC  48 8B C4                        mov rax, rsp
00AB15FF  48 81 EC 88 00 00 00            sub rsp, 0x88
00AB1606  83 60 10 00                     and dword ptr [rax + 0x10], 0
00AB160A  0F 57 C0                        xorps xmm0, xmm0
00AB160D  83 60 08 00                     and dword ptr [rax + 8], 0
00AB1611  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
00AB1615  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
00AB1619  84 C9                           test cl, cl
00AB161B  0F 84 8F 00 00 00               je 0x140ab16b0
00AB1621  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
00AB162A  4C 8D 40 D8                     lea r8, [rax - 0x28]
00AB162E  33 C9                           xor ecx, ecx
00AB1630  48 8B 92 B8 00 00 00            mov rdx, qword ptr [rdx + 0xb8]
00AB1637  E8 54 36 E1 FF                  call 0x1408c4c90
00AB163C  48 8B 05 55 57 51 00            mov rax, qword ptr [rip + 0x515755]
00AB1643  48 8D 8C 24 90 00 00 00         lea rcx, [rsp + 0x90]
00AB164B  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
00AB1650  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00AB1655  48 8D 8C 24 98 00 00 00         lea rcx, [rsp + 0x98]
00AB165D  45 33 C9                        xor r9d, r9d
00AB1660  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00AB1665  48 83 C0 4C                     add rax, 0x4c
00AB1669  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
00AB166E  48 8D 0D DB D9 09 00            lea rcx, [rip + 0x9d9db]
00AB1675  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AB167A  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00AB1680  41 8D 51 07                     lea edx, [r9 + 7]
00AB1684  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
00AB1689  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
00AB1691  E8 9A 55 8F FF                  call 0x1403a6c30
00AB1696  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00AB169B  E8 70 A0 DB FF                  call 0x14086b710
00AB16A0  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
00AB16A7  48 81 C4 88 00 00 00            add rsp, 0x88
00AB16AE  C3                              ret
00AB16AF  CC                              int3
00AB16B0  B8 22 00 00 C0                  mov eax, 0xc0000022
00AB16B5  EB F0                           jmp 0x140ab16a7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpCheckWakeTimerAccess(int a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int8 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (136);
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 24) = v_xmm0;
    if ((unsigned __int8)(a1) == 0) goto loc_00AB16B0;
    a1 = 0;
    result = SeCaptureSubjectContextEx(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), v_rsp - 40, a4);
    v_stack_m38 = v_stack_p8;
    a4 = 0;
    v_stack_m40 = v_stack_p10;
    result = (*(unsigned __int64 *)(v_rip + 5330773)) + (76);
    v_stack_m48 = 1;
    v_stack_m50 = result;
    v_stack_m68 = 1;
    result = SeAccessCheckWithHint(v_rip + 645595, a4 + 7, v_stack_m28, a4);
    result = SeReleaseSubjectContext(v_stack_m28, a4 + 7, v_stack_m28, a4);
loc_00AB16A7:
    v_rsp = (v_rsp) + (136);
    return (unsigned int)(v_stack_p8);
loc_00AB16B0:
    goto loc_00AB16A7;
}
```

## 5. (Beta) C Style

```c
int64_t ExpCheckWakeTimerAccess(int32_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint8_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (136);
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x18) = v_xmm0;
    if ((uint8_t)(Arg1) == 0) goto loc_00AB16B0;
    Arg1 = 0;
    result = SeCaptureSubjectContextEx(Arg1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), local_rsp - 40, Arg4);
    v_stack_m38 = v_stack_p8;
    Arg4 = 0;
    v_stack_m40 = v_stack_p10;
    result = (*(uint64_t *)(v_rip + 0x515755)) + (76);
    v_stack_m48 = 1;
    v_stack_m50 = result;
    v_stack_m68 = 1;
    result = SeAccessCheckWithHint(v_rip + 645595, Arg4 + 7, v_stack_m28, Arg4);
    result = SeReleaseSubjectContext(v_stack_m28, Arg4 + 7, v_stack_m28, Arg4);
loc_00AB16A7:
    local_rsp = (local_rsp) + (136);
    return (uint32_t)(v_stack_p8);
loc_00AB16B0:
    goto loc_00AB16A7;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB15FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AB15FC[BB_00AB15FC]
  bb_00AB1621[BB_00AB1621]
  bb_00AB16A7[BB_00AB16A7]
  bb_00AB16AF[BB_00AB16AF]
  bb_00AB16B0[BB_00AB16B0]
  bb_00AB15FC -->|branch| bb_00AB16B0
  bb_00AB15FC -->|fallthrough| bb_00AB1621
  bb_00AB1621 -->|flow| bb_00AB16A7
  bb_00AB16AF -->|flow| bb_00AB16B0
  bb_00AB16B0 -->|branch| bb_00AB16A7
```
