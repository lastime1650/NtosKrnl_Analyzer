# PnpTraceDriverBlocked

- RVA: `0x0073CB88`–`0x0073CC79` (길이 `241` bytes)
- VA: `0x000000014073CB88`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AC058`
- 디코드: `53`개 명령, `241/241` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0073CBCB` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0073CBFA` → [tlgCreate1Sz_wchar_t](../../text/42/tlgCreate1Sz_wchar_t_function_00426198.md) (function, `0x00426198`)
- `0x0073CC5E` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0073CC6A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PiIsDriverBlocked](../99/PiIsDriverBlocked_function_0099C254.md) at `0x0099C46D`

### Static image references
- `0x0073CB96` → RVA `0x00E0A740` (`.data`; read)
- `0x0073CBA4` → RVA `0x00E06F90` (`.data`; read)
- `0x0073CC3B` → RVA `0x00046EFE` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x0073CBCB` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0073CBFA` → [tlgCreate1Sz_wchar_t](../../text/42/tlgCreate1Sz_wchar_t_function_00426198.md) (`PAGE` → `.text`)
  - `0x0073CC5E` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0073CC6A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0073CB88  40 55                           push rbp
0073CB8A  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
0073CB8F  48 81 EC C0 00 00 00            sub rsp, 0xc0
0073CB96  48 8B 05 A3 DB 6C 00            mov rax, qword ptr [rip + 0x6cdba3]
0073CB9D  48 33 C4                        xor rax, rsp
0073CBA0  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
0073CBA4  83 3D E5 A3 6C 00 05            cmp dword ptr [rip + 0x6ca3e5], 5
0073CBAB  45 8B D0                        mov r10d, r8d
0073CBAE  4C 8B C1                        mov r8, rcx
0073CBB1  4C 8B DA                        mov r11, rdx
0073CBB4  0F 86 A9 00 00 00               jbe 0x14073cc63
0073CBBA  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
0073CBC4  48 8D 0D C5 A3 6C 00            lea rcx, [rip + 0x6ca3c5]
0073CBCB  E8 D0 1E CF FF                  call 0x14042eaa0
0073CBD0  84 C0                           test al, al
0073CBD2  0F 84 8B 00 00 00               je 0x14073cc63
0073CBD8  83 65 03 00                     and dword ptr [rbp + 3], 0
0073CBDC  48 8D 45 CF                     lea rax, [rbp - 0x31]
0073CBE0  49 8B D0                        mov rdx, r8
0073CBE3  48 89 45 F7                     mov qword ptr [rbp - 9], rax
0073CBE7  48 8D 4D 07                     lea rcx, [rbp + 7]
0073CBEB  48 C7 45 CF 00 08 00 00         mov qword ptr [rbp - 0x31], 0x800
0073CBF3  C7 45 FF 08 00 00 00            mov dword ptr [rbp - 1], 8
0073CBFA  E8 99 95 CE FF                  call 0x140426198
0073CBFF  83 65 23 00                     and dword ptr [rbp + 0x23], 0
0073CC03  48 8D 45 C7                     lea rax, [rbp - 0x39]
0073CC07  83 65 33 00                     and dword ptr [rbp + 0x33], 0
0073CC0B  48 8D 0D 7E A3 6C 00            lea rcx, [rip + 0x6ca37e]
0073CC12  83 65 43 00                     and dword ptr [rbp + 0x43], 0
0073CC16  BA 04 00 00 00                  mov edx, 4
0073CC1B  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0073CC1F  45 33 C0                        xor r8d, r8d
0073CC22  48 8D 45 CB                     lea rax, [rbp - 0x35]
0073CC26  89 55 2F                        mov dword ptr [rbp + 0x2f], edx
0073CC29  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
0073CC2D  48 8D 45 D7                     lea rax, [rbp - 0x29]
0073CC31  44 89 4D CB                     mov dword ptr [rbp - 0x35], r9d
0073CC35  45 33 C9                        xor r9d, r9d
0073CC38  89 55 3F                        mov dword ptr [rbp + 0x3f], edx
0073CC3B  48 8D 15 BC A2 90 FF            lea rdx, [rip - 0x6f5d44]
0073CC42  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0073CC47  C7 44 24 20 07 00 00 00         mov dword ptr [rsp + 0x20], 7
0073CC4F  4C 89 5D 17                     mov qword ptr [rbp + 0x17], r11
0073CC53  C7 45 1F 10 00 00 00            mov dword ptr [rbp + 0x1f], 0x10
0073CC5A  44 89 55 C7                     mov dword ptr [rbp - 0x39], r10d
0073CC5E  E8 7D 94 CE FF                  call 0x1404260e0
0073CC63  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
0073CC67  48 33 CC                        xor rcx, rsp
0073CC6A  E8 D1 F9 F6 FF                  call 0x1406ac640
0073CC6F  48 81 C4 C0 00 00 00            add rsp, 0xc0
0073CC76  5D                              pop rbp
0073CC77  C3                              ret
0073CC78  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpTraceDriverBlocked(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
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
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m5F;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m94;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;

    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 7134115)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 7119845)) <= 5) goto loc_0073CC63;
    result = tlgKeywordOn(v_rip + 7119813, a2, a1, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m90;
        a2 = a1;
        v_stack_m68 = result;
        a1 = v_stack_m58;
        v_stack_m90 = 0x800ULL;
        v_stack_m60 = 8;
        result = tlgCreate1Sz_wchar_t(a1, a2, a1, a4);
        result = v_stack_m98;
        a1 = v_rip + 7119742;
        a2 = 4;
        v_stack_m38 = result;
        a3 = 0;
        result = v_stack_m94;
        v_stack_m30 = (unsigned int)(a2);
        v_stack_m28 = result;
        result = v_stack_m88;
        v_stack_m94 = a4;
        a4 = 0;
        v_stack_m20 = (unsigned int)(a2);
        a2 = v_rip - 7298372;
        v_stack_mA0 = result;
        v_stack_mA8 = 7;
        v_stack_m48 = a2;
        v_stack_m40 = 16;
        v_stack_m98 = (unsigned int)((unsigned int)(a3));
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (192);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PnpTraceDriverBlocked(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
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
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m5F;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m94;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;

    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x6CDBA3)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x6CA3E5)) <= 5) goto loc_0073CC63;
    result = tlgKeywordOn(v_rip + 7119813, Arg2, Arg1, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m90;
        Arg2 = Arg1;
        v_stack_m68 = result;
        Arg1 = v_stack_m58;
        v_stack_m90 = 0x800ULL;
        v_stack_m60 = 8;
        result = tlgCreate1Sz_wchar_t(Arg1, Arg2, Arg1, Arg4);
        result = v_stack_m98;
        Arg1 = v_rip + 7119742;
        Arg2 = 4;
        v_stack_m38 = result;
        Arg3 = 0;
        result = v_stack_m94;
        v_stack_m30 = (uint32_t)(Arg2);
        v_stack_m28 = result;
        result = v_stack_m88;
        v_stack_m94 = Arg4;
        Arg4 = 0;
        v_stack_m20 = (uint32_t)(Arg2);
        Arg2 = v_rip - 7298372;
        v_stack_mA0 = result;
        v_stack_mA8 = 7;
        v_stack_m48 = Arg2;
        v_stack_m40 = 16;
        v_stack_m98 = (uint32_t)((uint32_t)(Arg3));
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (192);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0073CB88&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0073CB88[BB_0073CB88]
  bb_0073CBBA[BB_0073CBBA]
  bb_0073CBD8[BB_0073CBD8]
  bb_0073CC63[BB_0073CC63]
  bb_0073CC78[BB_0073CC78]
  bb_0073CB88 -->|branch| bb_0073CC63
  bb_0073CB88 -->|fallthrough| bb_0073CBBA
  bb_0073CBBA -->|branch| bb_0073CC63
  bb_0073CBBA -->|fallthrough| bb_0073CBD8
  bb_0073CBD8 -->|flow| bb_0073CC63
```
