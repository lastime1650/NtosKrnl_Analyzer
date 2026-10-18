# TtmiLogDeviceDepartureNotified

- RVA: `0x00779808`–`0x0077991A` (길이 `274` bytes)
- VA: `0x0000000140779808`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C8F70`
- 디코드: `63`개 명령, `274/274` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00779852` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0077986F` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x007798EF` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x007798FB` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmNotifyDeviceDeparture](TtmNotifyDeviceDeparture_function_007757F0.md) at `0x00775892`

### Static image references
- `0x00779823` → RVA `0x00E0A740` (`.data`; read)
- `0x00779831` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x00779878` → RVA `0x00051BC9` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00779852` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0077986F` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x007798EF` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x007798FB` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00779808  48 8B C4                        mov rax, rsp
0077980B  48 89 58 08                     mov qword ptr [rax + 8], rbx
0077980F  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00779813  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
00779817  55                              push rbp
00779818  48 8D 68 A1                     lea rbp, [rax - 0x5f]
0077981C  48 81 EC C0 00 00 00            sub rsp, 0xc0
00779823  48 8B 05 16 0F 69 00            mov rax, qword ptr [rip + 0x690f16]
0077982A  48 33 C4                        xor rax, rsp
0077982D  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
00779831  83 3D 90 F0 85 00 05            cmp dword ptr [rip + 0x85f090], 5
00779838  41 8A D8                        mov bl, r8b
0077983B  48 8B FA                        mov rdi, rdx
0077983E  8B F1                           mov esi, ecx
00779840  0F 86 AE 00 00 00               jbe 0x1407798f4
00779846  BA 01 00 00 00                  mov edx, 1
0077984B  48 8D 0D 76 F0 85 00            lea rcx, [rip + 0x85f076]
00779852  E8 49 52 CB FF                  call 0x14042eaa0
00779857  84 C0                           test al, al
00779859  0F 84 95 00 00 00               je 0x1407798f4
0077985F  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00779868  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
0077986F  E8 7C 60 AB FF                  call 0x14022f8f0
00779874  83 65 13 00                     and dword ptr [rbp + 0x13], 0
00779878  48 8D 15 4A 83 8D FF            lea rdx, [rip - 0x727cb6]
0077987F  83 65 23 00                     and dword ptr [rbp + 0x23], 0
00779883  B9 04 00 00 00                  mov ecx, 4
00779888  83 65 33 00                     and dword ptr [rbp + 0x33], 0
0077988C  45 33 C9                        xor r9d, r9d
0077988F  83 65 43 00                     and dword ptr [rbp + 0x43], 0
00779893  45 33 C0                        xor r8d, r8d
00779896  89 45 CB                        mov dword ptr [rbp - 0x35], eax
00779899  48 8D 45 CB                     lea rax, [rbp - 0x35]
0077989D  48 89 45 07                     mov qword ptr [rbp + 7], rax
007798A1  48 8D 45 CF                     lea rax, [rbp - 0x31]
007798A5  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
007798A9  48 8D 45 D7                     lea rax, [rbp - 0x29]
007798AD  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
007798B1  48 8D 45 C7                     lea rax, [rbp - 0x39]
007798B5  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
007798B9  48 8D 45 E7                     lea rax, [rbp - 0x19]
007798BD  89 4D 0F                        mov dword ptr [rbp + 0xf], ecx
007798C0  89 4D 1F                        mov dword ptr [rbp + 0x1f], ecx
007798C3  48 8D 0D FE EF 85 00            lea rcx, [rip + 0x85effe]
007798CA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007798CF  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
007798D7  89 75 CF                        mov dword ptr [rbp - 0x31], esi
007798DA  48 89 7D D7                     mov qword ptr [rbp - 0x29], rdi
007798DE  C7 45 2F 08 00 00 00            mov dword ptr [rbp + 0x2f], 8
007798E5  88 5D C7                        mov byte ptr [rbp - 0x39], bl
007798E8  C7 45 3F 01 00 00 00            mov dword ptr [rbp + 0x3f], 1
007798EF  E8 EC C7 CA FF                  call 0x1404260e0
007798F4  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
007798F8  48 33 CC                        xor rcx, rsp
007798FB  E8 40 2D F3 FF                  call 0x1406ac640
00779900  4C 8D 9C 24 C0 00 00 00         lea r11, [rsp + 0xc0]
00779908  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
0077990C  49 8B 73 18                     mov rsi, qword ptr [r11 + 0x18]
00779910  49 8B 7B 20                     mov rdi, qword ptr [r11 + 0x20]
00779914  49 8B E3                        mov rsp, r11
00779917  5D                              pop rbp
00779918  C3                              ret
00779919  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogDeviceDepartureNotified(int a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 6885142)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 71) = result;
    if ((*(unsigned int *)(v_rip + 8777872)) <= 5) goto loc_007798F4;
    result = tlgKeywordOn(v_rip + 8777846, 1, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(a1 + 184);
        result = PsGetProcessSessionIdEx(a1, 1, a3, a4);
        a2 = v_rip - 7503030;
        a1 = 4;
        a4 = 0;
        a3 = 0;
        *(unsigned int *)(v_rsp - 95 - 53) = (unsigned int)(result);
        result = v_rsp - 95 - 53;
        *(unsigned __int64 *)(v_rsp - 95 + 7) = result;
        result = v_rsp - 95 - 49;
        *(unsigned __int64 *)(v_rsp - 95 + 23) = result;
        result = v_rsp - 95 - 41;
        *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
        result = v_rsp - 95 - 57;
        *(unsigned __int64 *)(v_rsp - 95 + 55) = result;
        result = v_rsp - 95 - 25;
        *(unsigned int *)(v_rsp - 95 + 15) = a1;
        *(unsigned int *)(v_rsp - 95 + 31) = a1;
        a1 = v_rip + 8777726;
        v_stack_mA0 = result;
        v_stack_mA8 = 6;
        *(unsigned int *)(v_rsp - 95 - 49) = (unsigned int)((unsigned int)(a1));
        *(unsigned __int64 *)(v_rsp - 95 - 41) = a2;
        *(unsigned int *)(v_rsp - 95 + 47) = 8;
        *(unsigned __int8 *)(v_rsp - 95 - 57) = (unsigned __int8)((unsigned __int8)(a3));
        *(unsigned int *)(v_rsp - 95 + 63) = 1;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 71)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogDeviceDepartureNotified(int32_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m8;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x690F16)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x47) = result;
    if ((*(uint32_t *)(v_rip + 0x85F090)) <= 5) goto loc_007798F4;
    result = tlgKeywordOn(v_rip + 8777846, 1, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(Arg1 + 0xB8);
        result = PsGetProcessSessionIdEx(Arg1, 1, Arg3, Arg4);
        Arg2 = v_rip - 7503030;
        Arg1 = 4;
        Arg4 = 0;
        Arg3 = 0;
        *(uint32_t *)(local_rsp - 0x5F - 0x35) = (uint32_t)(result);
        result = local_rsp - 95 - 53;
        *(uint64_t *)(local_rsp - 0x5F + 0x7) = result;
        result = local_rsp - 95 - 49;
        *(uint64_t *)(local_rsp - 0x5F + 0x17) = result;
        result = local_rsp - 95 - 41;
        *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
        result = local_rsp - 95 - 57;
        *(uint64_t *)(local_rsp - 0x5F + 0x37) = result;
        result = local_rsp - 95 - 25;
        *(uint32_t *)(local_rsp - 0x5F + 0xF) = Arg1;
        *(uint32_t *)(local_rsp - 0x5F + 0x1F) = Arg1;
        Arg1 = v_rip + 8777726;
        v_stack_mA0 = result;
        v_stack_mA8 = 6;
        *(uint32_t *)(local_rsp - 0x5F - 0x31) = (uint32_t)((uint32_t)(Arg1));
        *(uint64_t *)(local_rsp - 0x5F - 0x29) = Arg2;
        *(uint32_t *)(local_rsp - 0x5F + 0x2F) = 8;
        *(uint8_t *)(local_rsp - 0x5F - 0x39) = (uint8_t)((uint8_t)(Arg3));
        *(uint32_t *)(local_rsp - 0x5F + 0x3F) = 1;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x47)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00779808&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00779808[BB_00779808]
  bb_00779846[BB_00779846]
  bb_0077985F[BB_0077985F]
  bb_007798F4[BB_007798F4]
  bb_00779919[BB_00779919]
  bb_00779808 -->|branch| bb_007798F4
  bb_00779808 -->|fallthrough| bb_00779846
  bb_00779846 -->|branch| bb_007798F4
  bb_00779846 -->|fallthrough| bb_0077985F
  bb_0077985F -->|flow| bb_007798F4
```
