# PspIumVerifyParentSd

- RVA: `0x00787D04`–`0x00787DB1` (길이 `173` bytes)
- VA: `0x0000000140787D04`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CF3D8`
- 디코드: `44`개 명령, `173/173` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00787D37` → [SeConvertStringSecurityDescriptorToSecurityDescriptor](../../text/48/SeConvertStringSecurityDescriptorToSecurityDescriptor_function_00480000.md) (function, `0x00480000`)
- `0x00787D47` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x00787D8B` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (function, `0x003A6BC0`)
- `0x00787D94` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00787D9F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [sub_006F88AE](../../text/6F/Unknown_function_006F88AE.md) at `0x006F8BDB`

### Static image references
- `0x00787D74` → RVA `0x00E0C5A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00787D37` → [SeConvertStringSecurityDescriptorToSecurityDescriptor](../../text/48/SeConvertStringSecurityDescriptorToSecurityDescriptor_function_00480000.md) (`PAGE` → `.text`)
  - `0x00787D8B` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (`PAGE` → `.text`)
  - `0x00787D9F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00787D04  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
00787D08  55                              push rbp
00787D09  48 8B EC                        mov rbp, rsp
00787D0C  48 81 EC 80 00 00 00            sub rsp, 0x80
00787D13  48 83 65 D8 00                  and qword ptr [rbp - 0x28], 0
00787D18  4C 8D 4D D0                     lea r9, [rbp - 0x30]
00787D1C  83 65 28 00                     and dword ptr [rbp + 0x28], 0
00787D20  49 8B C0                        mov rax, r8
00787D23  0F 57 C0                        xorps xmm0, xmm0
00787D26  4C 8D 45 D8                     lea r8, [rbp - 0x28]
00787D2A  8B D1                           mov edx, ecx
00787D2C  48 8B C8                        mov rcx, rax
00787D2F  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00787D33  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00787D37  E8 C4 82 CF FF                  call 0x140480000
00787D3C  89 45 18                        mov dword ptr [rbp + 0x18], eax
00787D3F  85 C0                           test eax, eax
00787D41  78 64                           js 0x140787da7
00787D43  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00787D47  E8 D4 3A 0E 00                  call 0x14086b820
00787D4C  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00787D50  48 8D 45 18                     lea rax, [rbp + 0x18]
00787D54  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00787D59  48 8D 55 E0                     lea rdx, [rbp - 0x20]
00787D5D  48 8D 45 28                     lea rax, [rbp + 0x28]
00787D61  41 B9 80 00 00 00               mov r9d, 0x80
00787D67  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00787D6C  45 33 C0                        xor r8d, r8d
00787D6F  C6 44 24 38 01                  mov byte ptr [rsp + 0x38], 1
00787D74  48 8D 05 25 48 68 00            lea rax, [rip + 0x684825]
00787D7B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00787D80  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00787D86  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
00787D8B  E8 30 EE C1 FF                  call 0x1403a6bc0
00787D90  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00787D94  E8 77 39 0E 00                  call 0x14086b710
00787D99  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00787D9D  33 D2                           xor edx, edx
00787D9F  E8 CC AA 3F 00                  call 0x140b82870
00787DA4  8B 45 18                        mov eax, dword ptr [rbp + 0x18]
00787DA7  48 81 C4 80 00 00 00            add rsp, 0x80
00787DAE  5D                              pop rbp
00787DAF  C3                              ret
00787DB0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspIumVerifyParentSd(int a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int8 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned int v_stack_p10;
    unsigned int v_stack_p20;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (128);
    v_stack_m28 = v_xmm0;
    v_stack_m18 = v_xmm0;
    result = SeConvertStringSecurityDescriptorToSecurityDescriptor(a3, (unsigned int)(a1), v_stack_m30, v_stack_m38);
    v_stack_p10 = (unsigned int)(result);
    if (!(sign_flag)) {
        a1 = v_stack_m28;
        result = SeCaptureSubjectContext(a1, (unsigned int)(a1), v_stack_m30, v_stack_m38);
        a1 = v_stack_m30;
        result = v_stack_p10;
        v_stack_m40 = result;
        a2 = v_stack_m28;
        result = v_stack_p20;
        a4 = 128;
        v_stack_m48 = result;
        a3 = 0;
        v_stack_m50 = 1;
        result = v_rip + 6834213;
        v_stack_m58 = result;
        result = SeAccessCheck(a1, a2, a3, a4);
        a1 = v_stack_m28;
        result = SeReleaseSubjectContext(a1, a2, a3, a4);
        a1 = v_stack_m30;
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
        result = v_stack_p10;
    }
    v_rsp = (v_rsp) + (128);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspIumVerifyParentSd(int32_t Arg1, int32_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint8_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint32_t v_stack_p10;
    uint32_t v_stack_p20;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (128);
    v_stack_m28 = v_xmm0;
    v_stack_m18 = v_xmm0;
    result = SeConvertStringSecurityDescriptorToSecurityDescriptor(Arg3, (uint32_t)(Arg1), v_stack_m30, v_stack_m38);
    v_stack_p10 = (uint32_t)(result);
    if (!(sign_flag)) {
        Arg1 = v_stack_m28;
        result = SeCaptureSubjectContext(Arg1, (uint32_t)(Arg1), v_stack_m30, v_stack_m38);
        Arg1 = v_stack_m30;
        result = v_stack_p10;
        v_stack_m40 = result;
        Arg2 = v_stack_m28;
        result = v_stack_p20;
        a4 = 128;
        v_stack_m48 = result;
        Arg3 = 0;
        v_stack_m50 = 1;
        result = v_rip + 6834213;
        v_stack_m58 = result;
        result = SeAccessCheck(Arg1, Arg2, Arg3, a4);
        Arg1 = v_stack_m28;
        result = SeReleaseSubjectContext(Arg1, Arg2, Arg3, a4);
        Arg1 = v_stack_m30;
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, a4);
        result = v_stack_p10;
    }
    local_rsp = (local_rsp) + (128);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00787D04&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00787D04[BB_00787D04]
  bb_00787D43[BB_00787D43]
  bb_00787DA7[BB_00787DA7]
  bb_00787DB0[BB_00787DB0]
  bb_00787D04 -->|branch| bb_00787DA7
  bb_00787D04 -->|fallthrough| bb_00787D43
  bb_00787D43 -->|flow| bb_00787DA7
```
