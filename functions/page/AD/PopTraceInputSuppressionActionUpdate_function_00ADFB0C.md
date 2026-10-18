# PopTraceInputSuppressionActionUpdate

- RVA: `0x00ADFB0C`–`0x00ADFC9F` (길이 `403` bytes)
- VA: `0x0000000140ADFB0C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CC6F8`
- 디코드: `88`개 명령, `403/403` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00ADFB49` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00ADFC84` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00ADFC90` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopEvaluateInputSuppressionAction](../76/PopEvaluateInputSuppressionAction_function_00765454.md) at `0x007655A1`

### Static image references
- `0x00ADFB1A` → RVA `0x00E0A740` (`.data`; read)
- `0x00ADFB28` → RVA `0x00E07748` (`.data`; read)
- `0x00ADFB56` → RVA `0x00E6788C` (`.data`; read)
- `0x00ADFBE5` → RVA `0x00E67894` (`.data`; read)
- `0x00ADFC08` → RVA `0x00F0B6B0` (`.data`; read)
- `0x00ADFC3E` → RVA `0x00049958` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00ADFB49` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00ADFC84` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00ADFC90` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ADFB0C  40 55                           push rbp
00ADFB0E  48 8D 6C 24 E0                  lea rbp, [rsp - 0x20]
00ADFB13  48 81 EC 20 01 00 00            sub rsp, 0x120
00ADFB1A  48 8B 05 1F AC 32 00            mov rax, qword ptr [rip + 0x32ac1f]
00ADFB21  48 33 C4                        xor rax, rsp
00ADFB24  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00ADFB28  83 3D 19 7C 32 00 05            cmp dword ptr [rip + 0x327c19], 5
00ADFB2F  44 8A D2                        mov r10b, dl
00ADFB32  0F 86 51 01 00 00               jbe 0x140adfc89
00ADFB38  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
00ADFB42  48 8D 0D FF 7B 32 00            lea rcx, [rip + 0x327bff]
00ADFB49  E8 52 EF 94 FF                  call 0x14042eaa0
00ADFB4E  84 C0                           test al, al
00ADFB50  0F 84 33 01 00 00               je 0x140adfc89
00ADFB56  8A 05 30 7D 38 00               mov al, byte ptr [rip + 0x387d30]
00ADFB5C  48 8D 0D E5 7B 32 00            lea rcx, [rip + 0x327be5]
00ADFB63  83 64 24 7C 00                  and dword ptr [rsp + 0x7c], 0
00ADFB68  41 BB 01 00 00 00               mov r11d, 1
00ADFB6E  83 65 8C 00                     and dword ptr [rbp - 0x74], 0
00ADFB72  83 65 9C 00                     and dword ptr [rbp - 0x64], 0
00ADFB76  83 65 AC 00                     and dword ptr [rbp - 0x54], 0
00ADFB7A  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00ADFB7E  41 8D 53 07                     lea edx, [r11 + 7]
00ADFB82  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00ADFB87  44 88 44 24 32                  mov byte ptr [rsp + 0x32], r8b
00ADFB8C  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00ADFB91  45 84 C9                        test r9b, r9b
00ADFB94  48 8D 44 24 31                  lea rax, [rsp + 0x31]
00ADFB99  89 55 E8                        mov dword ptr [rbp - 0x18], edx
00ADFB9C  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00ADFBA0  0F 94 44 24 34                  sete byte ptr [rsp + 0x34]
00ADFBA5  83 65 BC 00                     and dword ptr [rbp - 0x44], 0
00ADFBA9  48 8D 44 24 32                  lea rax, [rsp + 0x32]
00ADFBAE  83 65 CC 00                     and dword ptr [rbp - 0x34], 0
00ADFBB2  45 33 C9                        xor r9d, r9d
00ADFBB5  83 65 DC 00                     and dword ptr [rbp - 0x24], 0
00ADFBB9  45 33 C0                        xor r8d, r8d
00ADFBBC  83 65 EC 00                     and dword ptr [rbp - 0x14], 0
00ADFBC0  83 65 FC 00                     and dword ptr [rbp - 4], 0
00ADFBC4  83 65 0C 00                     and dword ptr [rbp + 0xc], 0
00ADFBC8  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00ADFBCC  8A 45 50                        mov al, byte ptr [rbp + 0x50]
00ADFBCF  88 44 24 33                     mov byte ptr [rsp + 0x33], al
00ADFBD3  48 8D 44 24 33                  lea rax, [rsp + 0x33]
00ADFBD8  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00ADFBDC  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00ADFBE1  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00ADFBE5  8A 05 A9 7C 38 00               mov al, byte ptr [rip + 0x387ca9]
00ADFBEB  88 44 24 35                     mov byte ptr [rsp + 0x35], al
00ADFBEF  48 8D 44 24 35                  lea rax, [rsp + 0x35]
00ADFBF4  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00ADFBF8  8B 45 60                        mov eax, dword ptr [rbp + 0x60]
00ADFBFB  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00ADFBFF  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00ADFC04  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00ADFC08  48 8B 05 A1 BA 42 00            mov rax, qword ptr [rip + 0x42baa1]
00ADFC0F  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00ADFC14  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00ADFC19  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00ADFC1D  8A 45 68                        mov al, byte ptr [rbp + 0x68]
00ADFC20  88 44 24 36                     mov byte ptr [rsp + 0x36], al
00ADFC24  48 8D 44 24 36                  lea rax, [rsp + 0x36]
00ADFC29  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00ADFC2D  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00ADFC32  48 89 45 00                     mov qword ptr [rbp], rax
00ADFC36  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00ADFC3B  89 55 08                        mov dword ptr [rbp + 8], edx
00ADFC3E  48 8D 15 13 9D 56 FF            lea rdx, [rip - 0xa962ed]
00ADFC45  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00ADFC4A  C7 44 24 20 0C 00 00 00         mov dword ptr [rsp + 0x20], 0xc
00ADFC52  44 89 5C 24 78                  mov dword ptr [rsp + 0x78], r11d
00ADFC57  44 88 54 24 31                  mov byte ptr [rsp + 0x31], r10b
00ADFC5C  44 89 5D 88                     mov dword ptr [rbp - 0x78], r11d
00ADFC60  44 89 5D 98                     mov dword ptr [rbp - 0x68], r11d
00ADFC64  44 89 5D A8                     mov dword ptr [rbp - 0x58], r11d
00ADFC68  44 89 5D B8                     mov dword ptr [rbp - 0x48], r11d
00ADFC6C  44 89 5D C8                     mov dword ptr [rbp - 0x38], r11d
00ADFC70  C7 45 D8 04 00 00 00            mov dword ptr [rbp - 0x28], 4
00ADFC77  44 89 5D F8                     mov dword ptr [rbp - 8], r11d
00ADFC7B  48 C7 44 24 48 00 00 00 01      mov qword ptr [rsp + 0x48], 0x1000000
00ADFC84  E8 57 64 94 FF                  call 0x1404260e0
00ADFC89  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00ADFC8D  48 33 CC                        xor rcx, rsp
00ADFC90  E8 AB C9 BC FF                  call 0x1406ac640
00ADFC95  48 81 C4 20 01 00 00            add rsp, 0x120
00ADFC9C  5D                              pop rbp
00ADFC9D  C3                              ret
00ADFC9E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopTraceInputSuppressionActionUpdate(__int64 a1, unsigned __int8 a2, int a3, int a4, unsigned __int8 a5, __int64 a6, unsigned int a7, unsigned __int8 a8)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned __int8 v_stack_mF2;
    unsigned __int8 v_stack_mF3;
    unsigned __int8 v_stack_mF4;
    unsigned __int8 v_stack_mF5;
    unsigned __int8 v_stack_mF6;
    unsigned __int64 v_stack_mF7;
    unsigned __int8 v_stack_mF8;

    v_rsp = (v_rsp) - (288);
    result = (*(unsigned __int64 *)(v_rip + 3320863)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 3308569)) <= 5) goto loc_00ADFC89;
    result = tlgKeywordOn(v_rip + 3308543, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned __int8 *)(v_rip + 3702064);
        a1 = v_rip + 3308517;
        v_r11 = 1;
        v_stack_mF8 = (unsigned __int8)(result);
        a2 = v_r11 + 7;
        result = v_stack_mF8;
        v_stack_mF6 = (unsigned __int8)(a3);
        v_stack_mB8 = result;
        result = v_stack_mF7;
        v_stack_m40 = a2;
        v_stack_mA8 = result;
        result = v_stack_mF6;
        a4 = 0;
        a3 = 0;
        v_stack_m98 = result;
        result = a5;
        v_stack_mF5 = (unsigned __int8)(result);
        result = v_stack_mF5;
        v_stack_m88 = result;
        result = v_stack_mF4;
        v_stack_m78 = result;
        result = *(unsigned __int8 *)(v_rip + 3701929);
        v_stack_mF3 = (unsigned __int8)(result);
        result = v_stack_mF3;
        v_stack_m68 = result;
        result = a7;
        v_stack_mF0 = (unsigned int)(result);
        result = v_stack_mF0;
        v_stack_m58 = result;
        result = *(unsigned __int64 *)(v_rip + 4373153);
        v_stack_mE8 = result;
        result = v_stack_mE8;
        v_stack_m48 = result;
        result = a8;
        v_stack_mF2 = (unsigned __int8)(result);
        result = v_stack_mF2;
        v_stack_m38 = result;
        result = v_stack_mE0;
        v_stack_m28 = result;
        result = v_stack_mD8;
        v_stack_m20 = a2;
        a2 = v_rip - 11100909;
        v_stack_m100 = result;
        v_stack_m108 = 12;
        v_stack_mB0 = (unsigned int)(v_r11);
        v_stack_mF7 = a2;
        v_stack_mA0 = (unsigned int)(v_r11);
        v_stack_m90 = (unsigned int)(v_r11);
        v_stack_m80 = (unsigned int)(v_r11);
        v_stack_m70 = (unsigned int)(v_r11);
        v_stack_m60 = (unsigned int)(v_r11);
        v_stack_m50 = 4;
        v_stack_m30 = (unsigned int)(v_r11);
        v_stack_mE0 = 0x1000000ULL;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (288);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopTraceInputSuppressionActionUpdate(int64_t Arg1, uint8_t Arg2, int32_t Arg3, int32_t Arg4, uint8_t Arg5, uint64_t Arg6, uint32_t Arg7, uint8_t Arg8)
{
    int64_t result;
    int64_t local_r11;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m108;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint8_t v_stack_mF2;
    uint8_t v_stack_mF3;
    uint8_t v_stack_mF4;
    uint8_t v_stack_mF5;
    uint8_t v_stack_mF6;
    uint64_t v_stack_mF7;
    uint8_t v_stack_mF8;

    local_rsp = (local_rsp) - (288);
    result = (*(uint64_t *)(v_rip + 0x32AC1F)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x327C19)) <= 5) goto loc_00ADFC89;
    result = tlgKeywordOn(v_rip + 3308543, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = *(uint8_t *)(v_rip + 0x387D30);
        Arg1 = v_rip + 3308517;
        local_r11 = 1;
        v_stack_mF8 = (uint8_t)(result);
        Arg2 = local_r11 + 7;
        result = v_stack_mF8;
        v_stack_mF6 = (uint8_t)(Arg3);
        v_stack_mB8 = result;
        result = v_stack_mF7;
        v_stack_m40 = Arg2;
        v_stack_mA8 = result;
        result = v_stack_mF6;
        Arg4 = 0;
        Arg3 = 0;
        v_stack_m98 = result;
        result = Arg5;
        v_stack_mF5 = (uint8_t)(result);
        result = v_stack_mF5;
        v_stack_m88 = result;
        result = v_stack_mF4;
        v_stack_m78 = result;
        result = *(uint8_t *)(v_rip + 0x387CA9);
        v_stack_mF3 = (uint8_t)(result);
        result = v_stack_mF3;
        v_stack_m68 = result;
        result = Arg7;
        v_stack_mF0 = (uint32_t)(result);
        result = v_stack_mF0;
        v_stack_m58 = result;
        result = *(uint64_t *)(v_rip + 0x42BAA1);
        v_stack_mE8 = result;
        result = v_stack_mE8;
        v_stack_m48 = result;
        result = Arg8;
        v_stack_mF2 = (uint8_t)(result);
        result = v_stack_mF2;
        v_stack_m38 = result;
        result = v_stack_mE0;
        v_stack_m28 = result;
        result = v_stack_mD8;
        v_stack_m20 = Arg2;
        Arg2 = v_rip - 11100909;
        v_stack_m100 = result;
        v_stack_m108 = 12;
        v_stack_mB0 = (uint32_t)(local_r11);
        v_stack_mF7 = Arg2;
        v_stack_mA0 = (uint32_t)(local_r11);
        v_stack_m90 = (uint32_t)(local_r11);
        v_stack_m80 = (uint32_t)(local_r11);
        v_stack_m70 = (uint32_t)(local_r11);
        v_stack_m60 = (uint32_t)(local_r11);
        v_stack_m50 = 4;
        v_stack_m30 = (uint32_t)(local_r11);
        v_stack_mE0 = 0x1000000ULL;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (288);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ADFB0C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00ADFB0C[BB_00ADFB0C]
  bb_00ADFB38[BB_00ADFB38]
  bb_00ADFB56[BB_00ADFB56]
  bb_00ADFC89[BB_00ADFC89]
  bb_00ADFC9E[BB_00ADFC9E]
  bb_00ADFB0C -->|branch| bb_00ADFC89
  bb_00ADFB0C -->|fallthrough| bb_00ADFB38
  bb_00ADFB38 -->|branch| bb_00ADFC89
  bb_00ADFB38 -->|fallthrough| bb_00ADFB56
  bb_00ADFB56 -->|flow| bb_00ADFC89
```
