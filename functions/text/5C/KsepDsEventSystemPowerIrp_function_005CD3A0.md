# KsepDsEventSystemPowerIrp

- RVA: `0x005CD3A0`–`0x005CD4B0` (길이 `272` bytes)
- VA: `0x00000001405CD3A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CB588`
- 디코드: `65`개 명령, `272/272` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x005CD3E4` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x005CD495` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x005CD4A1` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KseDsCallbackHookIrpPowerFunction](KseDsCallbackHookIrpPowerFunction_function_005CC200.md) at `0x005CC2D6`

### Static image references
- `0x005CD3BF` → RVA `0x00E0A740` (`.data`; read)
- `0x005CD3CD` → RVA `0x00E66CE0` (`.data`; read)
- `0x005CD3DD` → RVA `0x00022E60` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CD3A0  48 8B C4                        mov rax, rsp
005CD3A3  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
005CD3A7  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
005CD3AB  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
005CD3AF  48 89 48 08                     mov qword ptr [rax + 8], rcx
005CD3B3  55                              push rbp
005CD3B4  48 8D 68 B9                     lea rbp, [rax - 0x47]
005CD3B8  48 81 EC C0 00 00 00            sub rsp, 0xc0
005CD3BF  48 8B 05 7A D3 83 00            mov rax, qword ptr [rip + 0x83d37a]
005CD3C6  48 33 C4                        xor rax, rsp
005CD3C9  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
005CD3CD  48 8B 0D 0C 99 89 00            mov rcx, qword ptr [rip + 0x89990c]
005CD3D4  48 85 C9                        test rcx, rcx
005CD3D7  0F 84 BD 00 00 00               je 0x1405cd49a
005CD3DD  48 8D 15 7C 5A A5 FF            lea rdx, [rip - 0x5aa584]
005CD3E4  E8 67 50 DC FF                  call 0x140392450
005CD3E9  84 C0                           test al, al
005CD3EB  0F 84 A9 00 00 00               je 0x1405cd49a
005CD3F1  83 65 CB 00                     and dword ptr [rbp - 0x35], 0
005CD3F5  48 8D 45 4F                     lea rax, [rbp + 0x4f]
005CD3F9  83 65 DB 00                     and dword ptr [rbp - 0x25], 0
005CD3FD  48 8D 15 5C 5A A5 FF            lea rdx, [rip - 0x5aa5a4]
005CD404  83 65 EB 00                     and dword ptr [rbp - 0x15], 0
005CD408  B9 08 00 00 00                  mov ecx, 8
005CD40D  83 65 FB 00                     and dword ptr [rbp - 5], 0
005CD411  45 33 C9                        xor r9d, r9d
005CD414  83 65 0B 00                     and dword ptr [rbp + 0xb], 0
005CD418  45 33 C0                        xor r8d, r8d
005CD41B  83 65 1B 00                     and dword ptr [rbp + 0x1b], 0
005CD41F  83 65 2B 00                     and dword ptr [rbp + 0x2b], 0
005CD423  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
005CD427  48 8D 45 57                     lea rax, [rbp + 0x57]
005CD42B  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
005CD42F  48 8D 45 5F                     lea rax, [rbp + 0x5f]
005CD433  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
005CD437  48 8D 45 67                     lea rax, [rbp + 0x67]
005CD43B  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
005CD43F  48 8D 45 6F                     lea rax, [rbp + 0x6f]
005CD443  48 89 45 FF                     mov qword ptr [rbp - 1], rax
005CD447  48 8D 45 77                     lea rax, [rbp + 0x77]
005CD44B  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
005CD44F  48 8D 45 7F                     lea rax, [rbp + 0x7f]
005CD453  89 4D C7                        mov dword ptr [rbp - 0x39], ecx
005CD456  89 4D D7                        mov dword ptr [rbp - 0x29], ecx
005CD459  89 4D E7                        mov dword ptr [rbp - 0x19], ecx
005CD45C  B9 04 00 00 00                  mov ecx, 4
005CD461  48 89 45 1F                     mov qword ptr [rbp + 0x1f], rax
005CD465  48 8D 45 BF                     lea rax, [rbp - 0x41]
005CD469  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005CD46E  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
005CD476  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005CD47C  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005CD482  89 4D F7                        mov dword ptr [rbp - 9], ecx
005CD485  89 4D 07                        mov dword ptr [rbp + 7], ecx
005CD488  89 4D 17                        mov dword ptr [rbp + 0x17], ecx
005CD48B  89 4D 27                        mov dword ptr [rbp + 0x27], ecx
005CD48E  48 8B 0D 4B 98 89 00            mov rcx, qword ptr [rip + 0x89984b]
005CD495  E8 36 1C C9 FF                  call 0x14025f0d0
005CD49A  48 8B 4D 2F                     mov rcx, qword ptr [rbp + 0x2f]
005CD49E  48 33 CC                        xor rcx, rsp
005CD4A1  E8 9A F1 0D 00                  call 0x1406ac640
005CD4A6  48 81 C4 C0 00 00 00            add rsp, 0xc0
005CD4AD  5D                              pop rbp
005CD4AE  C3                              ret
005CD4AF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KsepDsEventSystemPowerIrp(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 8639354)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 71 + 47) = result;
    if (*(unsigned __int64 *)(v_rip + 9017612) == 0) goto loc_005CD49A;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 9017612), v_rip - 5940612, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_rsp - 71 + 79;
        a2 = v_rip - 5940644;
        a1 = 8;
        a4 = 0;
        a3 = 0;
        *(unsigned __int64 *)(v_rsp - 71 - 65) = result;
        result = v_rsp - 71 + 87;
        *(unsigned __int64 *)(v_rsp - 71 - 49) = result;
        result = v_rsp - 71 + 95;
        *(unsigned __int64 *)(v_rsp - 71 - 33) = result;
        result = v_rsp - 71 + 103;
        *(unsigned __int64 *)(v_rsp - 71 - 17) = result;
        result = v_rsp - 71 + 111;
        *(unsigned __int64 *)(v_rsp - 71 - 1) = result;
        result = v_rsp - 71 + 119;
        *(unsigned __int64 *)(v_rsp - 71 + 15) = result;
        result = v_rsp - 71 + 127;
        *(unsigned int *)(v_rsp - 71 - 57) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 71 - 41) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 71 - 25) = (unsigned int)(a1);
        a1 = 4;
        *(unsigned __int64 *)(v_rsp - 71 + 31) = result;
        result = v_rsp - 71 - 65;
        v_stack_m90 = result;
        v_stack_m98 = 7;
        *(unsigned int *)(v_rsp - 71 - 9) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 71 + 7) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 71 + 23) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 71 + 39) = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 9017419);
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 71 + 47)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (192);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KsepDsEventSystemPowerIrp(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x83D37A)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x47 + 0x2F) = result;
    if (*(uint64_t *)(v_rip + 0x89990C) == 0) goto loc_005CD49A;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x89990C), v_rip - 5940612, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = local_rsp - 71 + 79;
        Arg2 = v_rip - 5940644;
        Arg1 = 8;
        Arg4 = 0;
        Arg3 = 0;
        *(uint64_t *)(local_rsp - 0x47 - 0x41) = result;
        result = local_rsp - 71 + 87;
        *(uint64_t *)(local_rsp - 0x47 - 0x31) = result;
        result = local_rsp - 71 + 95;
        *(uint64_t *)(local_rsp - 0x47 - 0x21) = result;
        result = local_rsp - 71 + 103;
        *(uint64_t *)(local_rsp - 0x47 - 0x11) = result;
        result = local_rsp - 71 + 111;
        *(uint64_t *)(local_rsp - 0x47 - 0x1) = result;
        result = local_rsp - 71 + 119;
        *(uint64_t *)(local_rsp - 0x47 + 0xF) = result;
        result = local_rsp - 71 + 127;
        *(uint32_t *)(local_rsp - 0x47 - 0x39) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x47 - 0x29) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x47 - 0x19) = (uint32_t)(Arg1);
        Arg1 = 4;
        *(uint64_t *)(local_rsp - 0x47 + 0x1F) = result;
        result = local_rsp - 71 - 65;
        v_stack_m90 = result;
        v_stack_m98 = 7;
        *(uint32_t *)(local_rsp - 0x47 - 0x9) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x47 + 0x7) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x47 + 0x17) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x47 + 0x27) = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x89984B);
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x47 + 0x2F)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (192);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CD3A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CD3A0[BB_005CD3A0]
  bb_005CD3DD[BB_005CD3DD]
  bb_005CD3F1[BB_005CD3F1]
  bb_005CD49A[BB_005CD49A]
  bb_005CD4AF[BB_005CD4AF]
  bb_005CD3A0 -->|branch| bb_005CD49A
  bb_005CD3A0 -->|fallthrough| bb_005CD3DD
  bb_005CD3DD -->|branch| bb_005CD49A
  bb_005CD3DD -->|fallthrough| bb_005CD3F1
  bb_005CD3F1 -->|flow| bb_005CD49A
```
