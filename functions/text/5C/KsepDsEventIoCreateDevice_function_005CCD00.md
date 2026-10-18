# KsepDsEventIoCreateDevice

- RVA: `0x005CCD00`–`0x005CCE08` (길이 `264` bytes)
- VA: `0x00000001405CCD00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CB588`
- 디코드: `63`개 명령, `264/264` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x005CCD4B` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x005CCDED` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x005CCDF9` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KseDsHookIoCreateDevice](KseDsHookIoCreateDevice_function_005CC520.md) at `0x005CC58B`

### Static image references
- `0x005CCD1F` → RVA `0x00E0A740` (`.data`; read)
- `0x005CCD2D` → RVA `0x00E66CE0` (`.data`; read)
- `0x005CCD44` → RVA `0x00023610` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CCD00  48 8B C4                        mov rax, rsp
005CCD03  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
005CCD07  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
005CCD0B  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
005CCD0F  48 89 48 08                     mov qword ptr [rax + 8], rcx
005CCD13  55                              push rbp
005CCD14  48 8D 68 B1                     lea rbp, [rax - 0x4f]
005CCD18  48 81 EC C0 00 00 00            sub rsp, 0xc0
005CCD1F  48 8B 05 1A DA 83 00            mov rax, qword ptr [rip + 0x83da1a]
005CCD26  48 33 C4                        xor rax, rsp
005CCD29  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
005CCD2D  48 8B 0D AC 9F 89 00            mov rcx, qword ptr [rip + 0x899fac]
005CCD34  0F B6 45 77                     movzx eax, byte ptr [rbp + 0x77]
005CCD38  89 45 C7                        mov dword ptr [rbp - 0x39], eax
005CCD3B  48 85 C9                        test rcx, rcx
005CCD3E  0F 84 AE 00 00 00               je 0x1405ccdf2
005CCD44  48 8D 15 C5 68 A5 FF            lea rdx, [rip - 0x5a973b]
005CCD4B  E8 00 57 DC FF                  call 0x140392450
005CCD50  84 C0                           test al, al
005CCD52  0F 84 9A 00 00 00               je 0x1405ccdf2
005CCD58  83 65 E3 00                     and dword ptr [rbp - 0x1d], 0
005CCD5C  48 8D 45 57                     lea rax, [rbp + 0x57]
005CCD60  83 65 F3 00                     and dword ptr [rbp - 0xd], 0
005CCD64  48 8D 15 A5 68 A5 FF            lea rdx, [rip - 0x5a975b]
005CCD6B  83 65 03 00                     and dword ptr [rbp + 3], 0
005CCD6F  B9 08 00 00 00                  mov ecx, 8
005CCD74  83 65 13 00                     and dword ptr [rbp + 0x13], 0
005CCD78  45 33 C9                        xor r9d, r9d
005CCD7B  83 65 23 00                     and dword ptr [rbp + 0x23], 0
005CCD7F  45 33 C0                        xor r8d, r8d
005CCD82  83 65 33 00                     and dword ptr [rbp + 0x33], 0
005CCD86  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
005CCD8A  48 8D 45 5F                     lea rax, [rbp + 0x5f]
005CCD8E  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
005CCD92  48 8D 45 67                     lea rax, [rbp + 0x67]
005CCD96  48 89 45 F7                     mov qword ptr [rbp - 9], rax
005CCD9A  48 8D 45 6F                     lea rax, [rbp + 0x6f]
005CCD9E  48 89 45 07                     mov qword ptr [rbp + 7], rax
005CCDA2  48 8D 45 C7                     lea rax, [rbp - 0x39]
005CCDA6  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
005CCDAA  48 8D 45 7F                     lea rax, [rbp + 0x7f]
005CCDAE  89 4D DF                        mov dword ptr [rbp - 0x21], ecx
005CCDB1  89 4D EF                        mov dword ptr [rbp - 0x11], ecx
005CCDB4  B9 04 00 00 00                  mov ecx, 4
005CCDB9  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
005CCDBD  48 8D 45 D7                     lea rax, [rbp - 0x29]
005CCDC1  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005CCDC6  C7 44 24 30 06 00 00 00         mov dword ptr [rsp + 0x30], 6
005CCDCE  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005CCDD4  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005CCDDA  89 4D FF                        mov dword ptr [rbp - 1], ecx
005CCDDD  89 4D 0F                        mov dword ptr [rbp + 0xf], ecx
005CCDE0  89 4D 1F                        mov dword ptr [rbp + 0x1f], ecx
005CCDE3  89 4D 2F                        mov dword ptr [rbp + 0x2f], ecx
005CCDE6  48 8B 0D F3 9E 89 00            mov rcx, qword ptr [rip + 0x899ef3]
005CCDED  E8 DE 22 C9 FF                  call 0x14025f0d0
005CCDF2  48 8B 4D 37                     mov rcx, qword ptr [rbp + 0x37]
005CCDF6  48 33 CC                        xor rcx, rsp
005CCDF9  E8 42 F8 0D 00                  call 0x1406ac640
005CCDFE  48 81 C4 C0 00 00 00            add rsp, 0xc0
005CCE05  5D                              pop rbp
005CCE06  C3                              ret
005CCE07  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KsepDsEventIoCreateDevice(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 8641050)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 79 + 55) = result;
    *(unsigned int *)(v_rsp - 79 - 57) = (unsigned int)(*(unsigned __int8 *)(v_rsp - 79 + 119));
    if (*(unsigned __int64 *)(v_rip + 9019308) == 0) goto loc_005CCDF2;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 9019308), v_rip - 5936955, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_rsp - 79 + 87;
        a2 = v_rip - 5936987;
        a1 = 8;
        a4 = 0;
        a3 = 0;
        *(unsigned __int64 *)(v_rsp - 79 - 41) = result;
        result = v_rsp - 79 + 95;
        *(unsigned __int64 *)(v_rsp - 79 - 25) = result;
        result = v_rsp - 79 + 103;
        *(unsigned __int64 *)(v_rsp - 79 - 9) = result;
        result = v_rsp - 79 + 111;
        *(unsigned __int64 *)(v_rsp - 79 + 7) = result;
        result = v_rsp - 79 - 57;
        *(unsigned __int64 *)(v_rsp - 79 + 23) = result;
        result = v_rsp - 79 + 127;
        *(unsigned int *)(v_rsp - 79 - 33) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 79 - 17) = (unsigned int)(a1);
        a1 = 4;
        *(unsigned __int64 *)(v_rsp - 79 + 39) = result;
        result = v_rsp - 79 - 41;
        v_stack_m90 = result;
        v_stack_m98 = 6;
        *(unsigned int *)(v_rsp - 79 - 1) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 79 + 15) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 79 + 31) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 79 + 47) = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 9019123);
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 79 + 55)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (192);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KsepDsEventIoCreateDevice(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x83DA1A)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x4F + 0x37) = result;
    *(uint32_t *)(local_rsp - 0x4F - 0x39) = (uint32_t)(*(uint8_t *)(local_rsp - 0x4F + 0x77));
    if (*(uint64_t *)(v_rip + 0x899FAC) == 0) goto loc_005CCDF2;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x899FAC), v_rip - 5936955, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = local_rsp - 79 + 87;
        Arg2 = v_rip - 5936987;
        Arg1 = 8;
        Arg4 = 0;
        Arg3 = 0;
        *(uint64_t *)(local_rsp - 0x4F - 0x29) = result;
        result = local_rsp - 79 + 95;
        *(uint64_t *)(local_rsp - 0x4F - 0x19) = result;
        result = local_rsp - 79 + 103;
        *(uint64_t *)(local_rsp - 0x4F - 0x9) = result;
        result = local_rsp - 79 + 111;
        *(uint64_t *)(local_rsp - 0x4F + 0x7) = result;
        result = local_rsp - 79 - 57;
        *(uint64_t *)(local_rsp - 0x4F + 0x17) = result;
        result = local_rsp - 79 + 127;
        *(uint32_t *)(local_rsp - 0x4F - 0x21) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x4F - 0x11) = (uint32_t)(Arg1);
        Arg1 = 4;
        *(uint64_t *)(local_rsp - 0x4F + 0x27) = result;
        result = local_rsp - 79 - 41;
        v_stack_m90 = result;
        v_stack_m98 = 6;
        *(uint32_t *)(local_rsp - 0x4F - 0x1) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x4F + 0xF) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x4F + 0x1F) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x4F + 0x2F) = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x899EF3);
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x4F + 0x37)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (192);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CCD00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CCD00[BB_005CCD00]
  bb_005CCD44[BB_005CCD44]
  bb_005CCD58[BB_005CCD58]
  bb_005CCDF2[BB_005CCDF2]
  bb_005CCE07[BB_005CCE07]
  bb_005CCD00 -->|branch| bb_005CCDF2
  bb_005CCD00 -->|fallthrough| bb_005CCD44
  bb_005CCD44 -->|branch| bb_005CCDF2
  bb_005CCD44 -->|fallthrough| bb_005CCD58
  bb_005CCD58 -->|flow| bb_005CCDF2
```
