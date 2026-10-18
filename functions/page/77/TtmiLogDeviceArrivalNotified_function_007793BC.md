# TtmiLogDeviceArrivalNotified

- RVA: `0x007793BC`–`0x00779500` (길이 `324` bytes)
- VA: `0x00000001407793BC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CDD4C`
- 디코드: `78`개 명령, `324/324` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0077940E` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0077942B` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x007794D1` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x007794DD` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmNotifyDeviceArrival](TtmNotifyDeviceArrival_function_007754F0.md) at `0x007757BD`

### Static image references
- `0x007793DB` → RVA `0x00E0A740` (`.data`; read)
- `0x007793E9` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x007794AD` → RVA `0x0005199A` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x0077940E` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0077942B` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x007794D1` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x007794DD` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007793BC  48 8B C4                        mov rax, rsp
007793BF  48 89 58 08                     mov qword ptr [rax + 8], rbx
007793C3  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
007793C7  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
007793CB  4C 89 70 20                     mov qword ptr [rax + 0x20], r14
007793CF  55                              push rbp
007793D0  48 8D 68 A9                     lea rbp, [rax - 0x57]
007793D4  48 81 EC E0 00 00 00            sub rsp, 0xe0
007793DB  48 8B 05 5E 13 69 00            mov rax, qword ptr [rip + 0x69135e]
007793E2  48 33 C4                        xor rax, rsp
007793E5  48 89 45 3F                     mov qword ptr [rbp + 0x3f], rax
007793E9  83 3D D8 F4 85 00 05            cmp dword ptr [rip + 0x85f4d8], 5
007793F0  41 8B D9                        mov ebx, r9d
007793F3  41 8B F8                        mov edi, r8d
007793F6  48 8B F2                        mov rsi, rdx
007793F9  44 8B F1                        mov r14d, ecx
007793FC  0F 86 D4 00 00 00               jbe 0x1407794d6
00779402  BA 01 00 00 00                  mov edx, 1
00779407  48 8D 0D BA F4 85 00            lea rcx, [rip + 0x85f4ba]
0077940E  E8 8D 56 CB FF                  call 0x14042eaa0
00779413  84 C0                           test al, al
00779415  0F 84 BB 00 00 00               je 0x1407794d6
0077941B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00779424  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
0077942B  E8 C0 64 AB FF                  call 0x14022f8f0
00779430  83 65 EB 00                     and dword ptr [rbp - 0x15], 0
00779434  48 8D 0D 8D F4 85 00            lea rcx, [rip + 0x85f48d]
0077943B  83 65 FB 00                     and dword ptr [rbp - 5], 0
0077943F  41 B8 04 00 00 00               mov r8d, 4
00779445  83 65 0B 00                     and dword ptr [rbp + 0xb], 0
00779449  45 33 C9                        xor r9d, r9d
0077944C  83 65 1B 00                     and dword ptr [rbp + 0x1b], 0
00779450  83 65 2B 00                     and dword ptr [rbp + 0x2b], 0
00779454  83 65 3B 00                     and dword ptr [rbp + 0x3b], 0
00779458  41 8D 50 04                     lea edx, [r8 + 4]
0077945C  89 45 9F                        mov dword ptr [rbp - 0x61], eax
0077945F  48 8D 45 9F                     lea rax, [rbp - 0x61]
00779463  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
00779467  48 8D 45 A3                     lea rax, [rbp - 0x5d]
0077946B  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
0077946F  48 8D 45 B7                     lea rax, [rbp - 0x49]
00779473  48 89 45 FF                     mov qword ptr [rbp - 1], rax
00779477  48 8D 45 A7                     lea rax, [rbp - 0x59]
0077947B  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
0077947F  48 8D 45 AB                     lea rax, [rbp - 0x55]
00779483  48 89 45 1F                     mov qword ptr [rbp + 0x1f], rax
00779487  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
0077948A  89 45 AF                        mov dword ptr [rbp - 0x51], eax
0077948D  48 8D 45 AF                     lea rax, [rbp - 0x51]
00779491  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
00779495  48 8D 45 BF                     lea rax, [rbp - 0x41]
00779499  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0077949E  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
007794A2  44 89 45 E7                     mov dword ptr [rbp - 0x19], r8d
007794A6  44 89 45 F7                     mov dword ptr [rbp - 9], r8d
007794AA  89 55 07                        mov dword ptr [rbp + 7], edx
007794AD  48 8D 15 E6 84 8D FF            lea rdx, [rip - 0x727b1a]
007794B4  44 89 45 17                     mov dword ptr [rbp + 0x17], r8d
007794B8  44 89 45 27                     mov dword ptr [rbp + 0x27], r8d
007794BC  44 89 45 37                     mov dword ptr [rbp + 0x37], r8d
007794C0  45 33 C0                        xor r8d, r8d
007794C3  44 89 75 A3                     mov dword ptr [rbp - 0x5d], r14d
007794C7  48 89 75 B7                     mov qword ptr [rbp - 0x49], rsi
007794CB  89 7D A7                        mov dword ptr [rbp - 0x59], edi
007794CE  89 5D AB                        mov dword ptr [rbp - 0x55], ebx
007794D1  E8 0A CC CA FF                  call 0x1404260e0
007794D6  48 8B 4D 3F                     mov rcx, qword ptr [rbp + 0x3f]
007794DA  48 33 CC                        xor rcx, rsp
007794DD  E8 5E 31 F3 FF                  call 0x1406ac640
007794E2  4C 8D 9C 24 E0 00 00 00         lea r11, [rsp + 0xe0]
007794EA  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
007794EE  49 8B 73 18                     mov rsi, qword ptr [r11 + 0x18]
007794F2  49 8B 7B 20                     mov rdi, qword ptr [r11 + 0x20]
007794F6  4D 8B 73 28                     mov r14, qword ptr [r11 + 0x28]
007794FA  49 8B E3                        mov rsp, r11
007794FD  5D                              pop rbp
007794FE  C3                              ret
007794FF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogDeviceArrivalNotified(int a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 32) = v_r14;
    v_rsp = (v_rsp) - (224);
    result = (*(unsigned __int64 *)(v_rip + 6886238)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 87 + 63) = result;
    if ((*(unsigned int *)(v_rip + 8778968)) <= 5) goto loc_007794D6;
    result = tlgKeywordOn(v_rip + 8778938, 1, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(a1 + 184);
        result = PsGetProcessSessionIdEx(a1, 1, a3, a4);
        a1 = v_rip + 8778893;
        a3 = 4;
        a4 = 0;
        a2 = a3 + 4;
        *(unsigned int *)(v_rsp - 87 - 97) = (unsigned int)(result);
        result = v_rsp - 87 - 97;
        *(unsigned __int64 *)(v_rsp - 87 - 33) = result;
        result = v_rsp - 87 - 93;
        *(unsigned __int64 *)(v_rsp - 87 - 17) = result;
        result = v_rsp - 87 - 73;
        *(unsigned __int64 *)(v_rsp - 87 - 1) = result;
        result = v_rsp - 87 - 89;
        *(unsigned __int64 *)(v_rsp - 87 + 15) = result;
        result = v_rsp - 87 - 85;
        *(unsigned __int64 *)(v_rsp - 87 + 31) = result;
        result = *(unsigned int *)(v_rsp - 87 + 127);
        *(unsigned int *)(v_rsp - 87 - 81) = (unsigned int)(result);
        result = v_rsp - 87 - 81;
        *(unsigned __int64 *)(v_rsp - 87 + 47) = result;
        result = v_rsp - 87 - 65;
        v_stack_mC0 = result;
        v_stack_mC8 = (unsigned int)(a2);
        *(unsigned int *)(v_rsp - 87 - 25) = a3;
        *(unsigned int *)(v_rsp - 87 - 9) = a3;
        *(unsigned int *)(v_rsp - 87 + 7) = (unsigned int)(a2);
        a2 = v_rip - 7502618;
        *(unsigned int *)(v_rsp - 87 + 23) = a3;
        *(unsigned int *)(v_rsp - 87 + 39) = a3;
        *(unsigned int *)(v_rsp - 87 + 55) = a3;
        a3 = 0;
        *(unsigned int *)(v_rsp - 87 - 93) = (unsigned int)((unsigned int)(a1));
        *(unsigned __int64 *)(v_rsp - 87 - 73) = a2;
        *(unsigned int *)(v_rsp - 87 - 89) = (unsigned int)((unsigned int)(a3));
        *(unsigned int *)(v_rsp - 87 - 85) = (unsigned int)((unsigned int)(a4));
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 87 + 63)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogDeviceArrivalNotified(int32_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint64_t *)(local_rsp + 0x20) = local_r14;
    local_rsp = (local_rsp) - (224);
    result = (*(uint64_t *)(v_rip + 0x69135E)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x57 + 0x3F) = result;
    if ((*(uint32_t *)(v_rip + 0x85F4D8)) <= 5) goto loc_007794D6;
    result = tlgKeywordOn(v_rip + 8778938, 1, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(Arg1 + 0xB8);
        result = PsGetProcessSessionIdEx(Arg1, 1, Arg3, Arg4);
        Arg1 = v_rip + 8778893;
        Arg3 = 4;
        Arg4 = 0;
        Arg2 = Arg3 + 4;
        *(uint32_t *)(local_rsp - 0x57 - 0x61) = (uint32_t)(result);
        result = local_rsp - 87 - 97;
        *(uint64_t *)(local_rsp - 0x57 - 0x21) = result;
        result = local_rsp - 87 - 93;
        *(uint64_t *)(local_rsp - 0x57 - 0x11) = result;
        result = local_rsp - 87 - 73;
        *(uint64_t *)(local_rsp - 0x57 - 0x1) = result;
        result = local_rsp - 87 - 89;
        *(uint64_t *)(local_rsp - 0x57 + 0xF) = result;
        result = local_rsp - 87 - 85;
        *(uint64_t *)(local_rsp - 0x57 + 0x1F) = result;
        result = *(uint32_t *)(local_rsp - 0x57 + 0x7F);
        *(uint32_t *)(local_rsp - 0x57 - 0x51) = (uint32_t)(result);
        result = local_rsp - 87 - 81;
        *(uint64_t *)(local_rsp - 0x57 + 0x2F) = result;
        result = local_rsp - 87 - 65;
        v_stack_mC0 = result;
        v_stack_mC8 = (uint32_t)(Arg2);
        *(uint32_t *)(local_rsp - 0x57 - 0x19) = Arg3;
        *(uint32_t *)(local_rsp - 0x57 - 0x9) = Arg3;
        *(uint32_t *)(local_rsp - 0x57 + 0x7) = (uint32_t)(Arg2);
        Arg2 = v_rip - 7502618;
        *(uint32_t *)(local_rsp - 0x57 + 0x17) = Arg3;
        *(uint32_t *)(local_rsp - 0x57 + 0x27) = Arg3;
        *(uint32_t *)(local_rsp - 0x57 + 0x37) = Arg3;
        Arg3 = 0;
        *(uint32_t *)(local_rsp - 0x57 - 0x5D) = (uint32_t)((uint32_t)(Arg1));
        *(uint64_t *)(local_rsp - 0x57 - 0x49) = Arg2;
        *(uint32_t *)(local_rsp - 0x57 - 0x59) = (uint32_t)((uint32_t)(Arg3));
        *(uint32_t *)(local_rsp - 0x57 - 0x55) = (uint32_t)((uint32_t)(Arg4));
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x57 + 0x3F)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007793BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007793BC[BB_007793BC]
  bb_00779402[BB_00779402]
  bb_0077941B[BB_0077941B]
  bb_007794D6[BB_007794D6]
  bb_007794FF[BB_007794FF]
  bb_007793BC -->|branch| bb_007794D6
  bb_007793BC -->|fallthrough| bb_00779402
  bb_00779402 -->|branch| bb_007794D6
  bb_00779402 -->|fallthrough| bb_0077941B
  bb_0077941B -->|flow| bb_007794D6
```
