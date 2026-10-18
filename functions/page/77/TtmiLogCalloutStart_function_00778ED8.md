# TtmiLogCalloutStart

- RVA: `0x00778ED8`–`0x0077900D` (길이 `309` bytes)
- VA: `0x0000000140778ED8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CDDEC`
- 디코드: `73`개 명령, `309/309` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00778F26` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00778F43` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x00778FE2` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00778FEE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmpStartCallout](TtmpStartCallout_function_00776AA4.md) at `0x00776BF0`

### Static image references
- `0x00778EF7` → RVA `0x00E0A740` (`.data`; read)
- `0x00778F05` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x00778FBF` → RVA `0x00051574` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00778F26` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00778F43` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x00778FE2` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00778FEE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00778ED8  48 8B C4                        mov rax, rsp
00778EDB  48 89 58 08                     mov qword ptr [rax + 8], rbx
00778EDF  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00778EE3  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00778EE7  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00778EEB  55                              push rbp
00778EEC  48 8D 68 A1                     lea rbp, [rax - 0x5f]
00778EF0  48 81 EC E0 00 00 00            sub rsp, 0xe0
00778EF7  48 8B 05 42 18 69 00            mov rax, qword ptr [rip + 0x691842]
00778EFE  48 33 C4                        xor rax, rsp
00778F01  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
00778F05  83 3D BC F9 85 00 05            cmp dword ptr [rip + 0x85f9bc], 5
00778F0C  41 8B D9                        mov ebx, r9d
00778F0F  48 8B FA                        mov rdi, rdx
00778F12  8B F1                           mov esi, ecx
00778F14  0F 86 CD 00 00 00               jbe 0x140778fe7
00778F1A  BA 01 00 00 00                  mov edx, 1
00778F1F  48 8D 0D A2 F9 85 00            lea rcx, [rip + 0x85f9a2]
00778F26  E8 75 5B CB FF                  call 0x14042eaa0
00778F2B  84 C0                           test al, al
00778F2D  0F 84 B4 00 00 00               je 0x140778fe7
00778F33  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00778F3C  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
00778F43  E8 A8 69 AB FF                  call 0x14022f8f0
00778F48  83 65 F3 00                     and dword ptr [rbp - 0xd], 0
00778F4C  48 8D 0D 75 F9 85 00            lea rcx, [rip + 0x85f975]
00778F53  83 65 03 00                     and dword ptr [rbp + 3], 0
00778F57  41 B8 04 00 00 00               mov r8d, 4
00778F5D  83 65 13 00                     and dword ptr [rbp + 0x13], 0
00778F61  45 33 C9                        xor r9d, r9d
00778F64  83 65 23 00                     and dword ptr [rbp + 0x23], 0
00778F68  83 65 33 00                     and dword ptr [rbp + 0x33], 0
00778F6C  83 65 43 00                     and dword ptr [rbp + 0x43], 0
00778F70  41 8D 50 04                     lea edx, [r8 + 4]
00778F74  89 45 A7                        mov dword ptr [rbp - 0x59], eax
00778F77  48 8D 45 A7                     lea rax, [rbp - 0x59]
00778F7B  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00778F7F  48 8D 45 AB                     lea rax, [rbp - 0x55]
00778F83  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00778F87  48 8D 45 B7                     lea rax, [rbp - 0x49]
00778F8B  48 89 45 07                     mov qword ptr [rbp + 7], rax
00778F8F  48 8D 45 2F                     lea rax, [rbp + 0x2f]
00778F93  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00778F97  48 8D 45 77                     lea rax, [rbp + 0x77]
00778F9B  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
00778F9F  48 8D 45 AF                     lea rax, [rbp - 0x51]
00778FA3  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
00778FA7  48 8D 45 C7                     lea rax, [rbp - 0x39]
00778FAB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00778FB0  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
00778FB4  44 89 45 EF                     mov dword ptr [rbp - 0x11], r8d
00778FB8  44 89 45 FF                     mov dword ptr [rbp - 1], r8d
00778FBC  89 55 0F                        mov dword ptr [rbp + 0xf], edx
00778FBF  48 8D 15 AE 85 8D FF            lea rdx, [rip - 0x727a52]
00778FC6  44 89 45 2F                     mov dword ptr [rbp + 0x2f], r8d
00778FCA  44 89 45 3F                     mov dword ptr [rbp + 0x3f], r8d
00778FCE  45 33 C0                        xor r8d, r8d
00778FD1  89 75 AB                        mov dword ptr [rbp - 0x55], esi
00778FD4  48 89 7D B7                     mov qword ptr [rbp - 0x49], rdi
00778FD8  C7 45 1F 02 00 00 00            mov dword ptr [rbp + 0x1f], 2
00778FDF  89 5D AF                        mov dword ptr [rbp - 0x51], ebx
00778FE2  E8 F9 D0 CA FF                  call 0x1404260e0
00778FE7  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
00778FEB  48 33 CC                        xor rcx, rsp
00778FEE  E8 4D 36 F3 FF                  call 0x1406ac640
00778FF3  4C 8D 9C 24 E0 00 00 00         lea r11, [rsp + 0xe0]
00778FFB  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
00778FFF  49 8B 73 18                     mov rsi, qword ptr [r11 + 0x18]
00779003  49 8B 7B 28                     mov rdi, qword ptr [r11 + 0x28]
00779007  49 8B E3                        mov rsp, r11
0077900A  5D                              pop rbp
0077900B  C3                              ret
0077900C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogCalloutStart(int a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned int *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (224);
    result = (*(unsigned __int64 *)(v_rip + 6887490)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 71) = result;
    if ((*(unsigned int *)(v_rip + 8780220)) <= 5) goto loc_00778FE7;
    result = tlgKeywordOn(v_rip + 8780194, 1, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(a1 + 184);
        result = PsGetProcessSessionIdEx(a1, 1, a3, a4);
        a1 = v_rip + 8780149;
        a3 = 4;
        a4 = 0;
        a2 = a3 + 4;
        *(unsigned int *)(v_rsp - 95 - 89) = (unsigned int)(result);
        result = v_rsp - 95 - 89;
        *(unsigned __int64 *)(v_rsp - 95 - 25) = result;
        result = v_rsp - 95 - 85;
        *(unsigned __int64 *)(v_rsp - 95 - 9) = result;
        result = v_rsp - 95 - 73;
        *(unsigned __int64 *)(v_rsp - 95 + 7) = result;
        result = v_rsp - 95 + 47;
        *(unsigned __int64 *)(v_rsp - 95 + 23) = result;
        result = v_rsp - 95 + 119;
        *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
        result = v_rsp - 95 - 81;
        *(unsigned __int64 *)(v_rsp - 95 + 55) = result;
        result = v_rsp - 95 - 57;
        v_stack_mC0 = result;
        v_stack_mC8 = (unsigned int)(a2);
        *(unsigned int *)(v_rsp - 95 - 17) = a3;
        *(unsigned int *)(v_rsp - 95 - 1) = a3;
        *(unsigned int *)(v_rsp - 95 + 15) = (unsigned int)(a2);
        a2 = v_rip - 7502418;
        *(unsigned int *)(v_rsp - 95 + 47) = a3;
        *(unsigned int *)(v_rsp - 95 + 63) = a3;
        a3 = 0;
        *(unsigned int *)(v_rsp - 95 - 85) = (unsigned int)((unsigned int)(a1));
        *(unsigned __int64 *)(v_rsp - 95 - 73) = a2;
        *(unsigned int *)(v_rsp - 95 + 31) = 2;
        *(unsigned int *)(v_rsp - 95 - 81) = (unsigned int)((unsigned int)(a4));
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 71)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogCalloutStart(int32_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (224);
    result = (*(uint64_t *)(v_rip + 0x691842)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x47) = result;
    if ((*(uint32_t *)(v_rip + 0x85F9BC)) <= 5) goto loc_00778FE7;
    result = tlgKeywordOn(v_rip + 8780194, 1, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(Arg1 + 0xB8);
        result = PsGetProcessSessionIdEx(Arg1, 1, Arg3, Arg4);
        Arg1 = v_rip + 8780149;
        Arg3 = 4;
        Arg4 = 0;
        Arg2 = Arg3 + 4;
        *(uint32_t *)(local_rsp - 0x5F - 0x59) = (uint32_t)(result);
        result = local_rsp - 95 - 89;
        *(uint64_t *)(local_rsp - 0x5F - 0x19) = result;
        result = local_rsp - 95 - 85;
        *(uint64_t *)(local_rsp - 0x5F - 0x9) = result;
        result = local_rsp - 95 - 73;
        *(uint64_t *)(local_rsp - 0x5F + 0x7) = result;
        result = local_rsp - 95 + 47;
        *(uint64_t *)(local_rsp - 0x5F + 0x17) = result;
        result = local_rsp - 95 + 119;
        *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
        result = local_rsp - 95 - 81;
        *(uint64_t *)(local_rsp - 0x5F + 0x37) = result;
        result = local_rsp - 95 - 57;
        v_stack_mC0 = result;
        v_stack_mC8 = (uint32_t)(Arg2);
        *(uint32_t *)(local_rsp - 0x5F - 0x11) = Arg3;
        *(uint32_t *)(local_rsp - 0x5F - 0x1) = Arg3;
        *(uint32_t *)(local_rsp - 0x5F + 0xF) = (uint32_t)(Arg2);
        Arg2 = v_rip - 7502418;
        *(uint32_t *)(local_rsp - 0x5F + 0x2F) = Arg3;
        *(uint32_t *)(local_rsp - 0x5F + 0x3F) = Arg3;
        Arg3 = 0;
        *(uint32_t *)(local_rsp - 0x5F - 0x55) = (uint32_t)((uint32_t)(Arg1));
        *(uint64_t *)(local_rsp - 0x5F - 0x49) = Arg2;
        *(uint32_t *)(local_rsp - 0x5F + 0x1F) = 2;
        *(uint32_t *)(local_rsp - 0x5F - 0x51) = (uint32_t)((uint32_t)(Arg4));
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x47)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00778ED8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00778ED8[BB_00778ED8]
  bb_00778F1A[BB_00778F1A]
  bb_00778F33[BB_00778F33]
  bb_00778FE7[BB_00778FE7]
  bb_0077900C[BB_0077900C]
  bb_00778ED8 -->|branch| bb_00778FE7
  bb_00778ED8 -->|fallthrough| bb_00778F1A
  bb_00778F1A -->|branch| bb_00778FE7
  bb_00778F1A -->|fallthrough| bb_00778F33
  bb_00778F33 -->|flow| bb_00778FE7
```
