# TtmiLogDeviceInputNotified

- RVA: `0x00779B94`–`0x00779CF7` (길이 `355` bytes)
- VA: `0x0000000140779B94`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C377C`
- 디코드: `83`개 명령, `355/355` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00779BE6` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00779C03` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x00779CC8` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00779CD4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmNotifyDeviceInput](TtmNotifyDeviceInput_function_007758B0.md) at `0x0077592E`

### Static image references
- `0x00779BB3` → RVA `0x00E0A740` (`.data`; read)
- `0x00779BC1` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x00779C0C` → RVA `0x00051CEB` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00779BE6` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00779C03` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x00779CC8` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00779CD4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00779B94  48 8B C4                        mov rax, rsp
00779B97  48 89 58 08                     mov qword ptr [rax + 8], rbx
00779B9B  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00779B9F  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
00779BA3  4C 89 70 20                     mov qword ptr [rax + 0x20], r14
00779BA7  55                              push rbp
00779BA8  48 8D 68 B1                     lea rbp, [rax - 0x4f]
00779BAC  48 81 EC F0 00 00 00            sub rsp, 0xf0
00779BB3  48 8B 05 86 0B 69 00            mov rax, qword ptr [rip + 0x690b86]
00779BBA  48 33 C4                        xor rax, rsp
00779BBD  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
00779BC1  83 3D 00 ED 85 00 05            cmp dword ptr [rip + 0x85ed00], 5
00779BC8  41 8A D9                        mov bl, r9b
00779BCB  41 8B F8                        mov edi, r8d
00779BCE  48 8B F2                        mov rsi, rdx
00779BD1  44 8B F1                        mov r14d, ecx
00779BD4  0F 86 F3 00 00 00               jbe 0x140779ccd
00779BDA  BA 01 00 00 00                  mov edx, 1
00779BDF  48 8D 0D E2 EC 85 00            lea rcx, [rip + 0x85ece2]
00779BE6  E8 B5 4E CB FF                  call 0x14042eaa0
00779BEB  84 C0                           test al, al
00779BED  0F 84 DA 00 00 00               je 0x140779ccd
00779BF3  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00779BFC  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
00779C03  E8 E8 5C AB FF                  call 0x14022f8f0
00779C08  83 65 D3 00                     and dword ptr [rbp - 0x2d], 0
00779C0C  48 8D 15 D8 80 8D FF            lea rdx, [rip - 0x727f28]
00779C13  83 65 E3 00                     and dword ptr [rbp - 0x1d], 0
00779C17  B9 04 00 00 00                  mov ecx, 4
00779C1C  83 65 F3 00                     and dword ptr [rbp - 0xd], 0
00779C20  45 33 C9                        xor r9d, r9d
00779C23  83 65 03 00                     and dword ptr [rbp + 3], 0
00779C27  45 33 C0                        xor r8d, r8d
00779C2A  83 65 13 00                     and dword ptr [rbp + 0x13], 0
00779C2E  83 65 23 00                     and dword ptr [rbp + 0x23], 0
00779C32  83 65 33 00                     and dword ptr [rbp + 0x33], 0
00779C36  89 45 8B                        mov dword ptr [rbp - 0x75], eax
00779C39  48 8D 45 8B                     lea rax, [rbp - 0x75]
00779C3D  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
00779C41  48 8D 45 8F                     lea rax, [rbp - 0x71]
00779C45  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
00779C49  48 8D 45 97                     lea rax, [rbp - 0x69]
00779C4D  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00779C51  48 8D 45 93                     lea rax, [rbp - 0x6d]
00779C55  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00779C59  48 8D 45 87                     lea rax, [rbp - 0x79]
00779C5D  48 89 45 07                     mov qword ptr [rbp + 7], rax
00779C61  8A 45 77                        mov al, byte ptr [rbp + 0x77]
00779C64  88 45 88                        mov byte ptr [rbp - 0x78], al
00779C67  48 8D 45 88                     lea rax, [rbp - 0x78]
00779C6B  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00779C6F  8A 45 7F                        mov al, byte ptr [rbp + 0x7f]
00779C72  88 45 89                        mov byte ptr [rbp - 0x77], al
00779C75  48 8D 45 89                     lea rax, [rbp - 0x77]
00779C79  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
00779C7D  48 8D 45 A7                     lea rax, [rbp - 0x59]
00779C81  89 4D CF                        mov dword ptr [rbp - 0x31], ecx
00779C84  89 4D DF                        mov dword ptr [rbp - 0x21], ecx
00779C87  89 4D FF                        mov dword ptr [rbp - 1], ecx
00779C8A  48 8D 0D 37 EC 85 00            lea rcx, [rip + 0x85ec37]
00779C91  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00779C96  C7 44 24 20 09 00 00 00         mov dword ptr [rsp + 0x20], 9
00779C9E  44 89 75 8F                     mov dword ptr [rbp - 0x71], r14d
00779CA2  48 89 75 97                     mov qword ptr [rbp - 0x69], rsi
00779CA6  C7 45 EF 08 00 00 00            mov dword ptr [rbp - 0x11], 8
00779CAD  89 7D 93                        mov dword ptr [rbp - 0x6d], edi
00779CB0  88 5D 87                        mov byte ptr [rbp - 0x79], bl
00779CB3  C7 45 0F 01 00 00 00            mov dword ptr [rbp + 0xf], 1
00779CBA  C7 45 1F 01 00 00 00            mov dword ptr [rbp + 0x1f], 1
00779CC1  C7 45 2F 01 00 00 00            mov dword ptr [rbp + 0x2f], 1
00779CC8  E8 13 C4 CA FF                  call 0x1404260e0
00779CCD  48 8B 4D 37                     mov rcx, qword ptr [rbp + 0x37]
00779CD1  48 33 CC                        xor rcx, rsp
00779CD4  E8 67 29 F3 FF                  call 0x1406ac640
00779CD9  4C 8D 9C 24 F0 00 00 00         lea r11, [rsp + 0xf0]
00779CE1  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
00779CE5  49 8B 73 18                     mov rsi, qword ptr [r11 + 0x18]
00779CE9  49 8B 7B 20                     mov rdi, qword ptr [r11 + 0x20]
00779CED  4D 8B 73 28                     mov r14, qword ptr [r11 + 0x28]
00779CF1  49 8B E3                        mov rsp, r11
00779CF4  5D                              pop rbp
00779CF5  C3                              ret
00779CF6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogDeviceInputNotified(int a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 32) = v_r14;
    v_rsp = (v_rsp) - (240);
    result = (*(unsigned __int64 *)(v_rip + 6884230)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 79 + 55) = result;
    if ((*(unsigned int *)(v_rip + 8776960)) <= 5) goto loc_00779CCD;
    result = tlgKeywordOn(v_rip + 8776930, 1, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(a1 + 184);
        result = PsGetProcessSessionIdEx(a1, 1, a3, a4);
        a2 = v_rip - 7503656;
        a1 = 4;
        a4 = 0;
        a3 = 0;
        *(unsigned int *)(v_rsp - 79 - 117) = (unsigned int)(result);
        result = v_rsp - 79 - 117;
        *(unsigned __int64 *)(v_rsp - 79 - 57) = result;
        result = v_rsp - 79 - 113;
        *(unsigned __int64 *)(v_rsp - 79 - 41) = result;
        result = v_rsp - 79 - 105;
        *(unsigned __int64 *)(v_rsp - 79 - 25) = result;
        result = v_rsp - 79 - 109;
        *(unsigned __int64 *)(v_rsp - 79 - 9) = result;
        result = v_rsp - 79 - 121;
        *(unsigned __int64 *)(v_rsp - 79 + 7) = result;
        result = *(unsigned __int8 *)(v_rsp - 79 + 119);
        *(unsigned __int8 *)(v_rsp - 79 - 120) = (unsigned __int8)(result);
        result = v_rsp - 79 - 120;
        *(unsigned __int64 *)(v_rsp - 79 + 23) = result;
        result = *(unsigned __int8 *)(v_rsp - 79 + 127);
        *(unsigned __int8 *)(v_rsp - 79 - 119) = (unsigned __int8)(result);
        result = v_rsp - 79 - 119;
        *(unsigned __int64 *)(v_rsp - 79 + 39) = result;
        result = v_rsp - 79 - 89;
        *(unsigned int *)(v_rsp - 79 - 49) = a1;
        *(unsigned int *)(v_rsp - 79 - 33) = a1;
        *(unsigned int *)(v_rsp - 79 - 1) = a1;
        a1 = v_rip + 8776759;
        v_stack_mD0 = result;
        v_stack_mD8 = 9;
        *(unsigned int *)(v_rsp - 79 - 113) = (unsigned int)((unsigned int)(a1));
        *(unsigned __int64 *)(v_rsp - 79 - 105) = a2;
        *(unsigned int *)(v_rsp - 79 - 17) = 8;
        *(unsigned int *)(v_rsp - 79 - 109) = (unsigned int)((unsigned int)(a3));
        *(unsigned __int8 *)(v_rsp - 79 - 121) = (unsigned __int8)((unsigned __int8)(a4));
        *(unsigned int *)(v_rsp - 79 + 15) = 1;
        *(unsigned int *)(v_rsp - 79 + 31) = 1;
        *(unsigned int *)(v_rsp - 79 + 47) = 1;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 79 + 55)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogDeviceInputNotified(int32_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint64_t *)(local_rsp + 0x20) = local_r14;
    local_rsp = (local_rsp) - (240);
    result = (*(uint64_t *)(v_rip + 0x690B86)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x4F + 0x37) = result;
    if ((*(uint32_t *)(v_rip + 0x85ED00)) <= 5) goto loc_00779CCD;
    result = tlgKeywordOn(v_rip + 8776930, 1, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(Arg1 + 0xB8);
        result = PsGetProcessSessionIdEx(Arg1, 1, Arg3, Arg4);
        Arg2 = v_rip - 7503656;
        Arg1 = 4;
        Arg4 = 0;
        Arg3 = 0;
        *(uint32_t *)(local_rsp - 0x4F - 0x75) = (uint32_t)(result);
        result = local_rsp - 79 - 117;
        *(uint64_t *)(local_rsp - 0x4F - 0x39) = result;
        result = local_rsp - 79 - 113;
        *(uint64_t *)(local_rsp - 0x4F - 0x29) = result;
        result = local_rsp - 79 - 105;
        *(uint64_t *)(local_rsp - 0x4F - 0x19) = result;
        result = local_rsp - 79 - 109;
        *(uint64_t *)(local_rsp - 0x4F - 0x9) = result;
        result = local_rsp - 79 - 121;
        *(uint64_t *)(local_rsp - 0x4F + 0x7) = result;
        result = *(uint8_t *)(local_rsp - 0x4F + 0x77);
        *(uint8_t *)(local_rsp - 0x4F - 0x78) = (uint8_t)(result);
        result = local_rsp - 79 - 120;
        *(uint64_t *)(local_rsp - 0x4F + 0x17) = result;
        result = *(uint8_t *)(local_rsp - 0x4F + 0x7F);
        *(uint8_t *)(local_rsp - 0x4F - 0x77) = (uint8_t)(result);
        result = local_rsp - 79 - 119;
        *(uint64_t *)(local_rsp - 0x4F + 0x27) = result;
        result = local_rsp - 79 - 89;
        *(uint32_t *)(local_rsp - 0x4F - 0x31) = Arg1;
        *(uint32_t *)(local_rsp - 0x4F - 0x21) = Arg1;
        *(uint32_t *)(local_rsp - 0x4F - 0x1) = Arg1;
        Arg1 = v_rip + 8776759;
        v_stack_mD0 = result;
        v_stack_mD8 = 9;
        *(uint32_t *)(local_rsp - 0x4F - 0x71) = (uint32_t)((uint32_t)(Arg1));
        *(uint64_t *)(local_rsp - 0x4F - 0x69) = Arg2;
        *(uint32_t *)(local_rsp - 0x4F - 0x11) = 8;
        *(uint32_t *)(local_rsp - 0x4F - 0x6D) = (uint32_t)((uint32_t)(Arg3));
        *(uint8_t *)(local_rsp - 0x4F - 0x79) = (uint8_t)((uint8_t)(Arg4));
        *(uint32_t *)(local_rsp - 0x4F + 0xF) = 1;
        *(uint32_t *)(local_rsp - 0x4F + 0x1F) = 1;
        *(uint32_t *)(local_rsp - 0x4F + 0x2F) = 1;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x4F + 0x37)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00779B94&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00779B94[BB_00779B94]
  bb_00779BDA[BB_00779BDA]
  bb_00779BF3[BB_00779BF3]
  bb_00779CCD[BB_00779CCD]
  bb_00779CF6[BB_00779CF6]
  bb_00779B94 -->|branch| bb_00779CCD
  bb_00779B94 -->|fallthrough| bb_00779BDA
  bb_00779BDA -->|branch| bb_00779CCD
  bb_00779BDA -->|fallthrough| bb_00779BF3
  bb_00779BF3 -->|flow| bb_00779CCD
```
