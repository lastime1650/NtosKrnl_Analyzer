# IopDumpTraceLoadDumpStackFailure

- RVA: `0x005952B8`–`0x005953C0` (길이 `264` bytes)
- VA: `0x00000001405952B8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BF3A4`
- 디코드: `57`개 명령, `264/264` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x005952D7` → [IopDumpIsTracingEnabled](../4F/IopDumpIsTracingEnabled_function_004FC5D0.md) (function, `0x004FC5D0`)
- `0x00595324` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x00595343` → [tlgKeywordOn](../42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x005953A5` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x005953B1` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [IoGetDumpStack](../../page/AD/IoGetDumpStack_function_00AD9D6C.md) at `0x00AD9DC2`

### Static image references
- `0x005952C9` → RVA `0x00E0A740` (`.data`; read)
- `0x005952E8` → RVA `0x00E65EF0` (`.data`; read)
- `0x005952EF` → RVA `0x00023308` (`.rdata`; read)
- `0x00595329` → RVA `0x00E06DE8` (`.data`; read)
- `0x00595358` → RVA `0x00045CFF` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005952B8  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
005952BC  55                              push rbp
005952BD  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
005952C2  48 81 EC B0 00 00 00            sub rsp, 0xb0
005952C9  48 8B 05 70 54 87 00            mov rax, qword ptr [rip + 0x875470]
005952D0  48 33 C4                        xor rax, rsp
005952D3  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
005952D7  E8 F4 72 F6 FF                  call 0x1404fc5d0
005952DC  84 C0                           test al, al
005952DE  74 49                           je 0x140595329
005952E0  83 65 03 00                     and dword ptr [rbp + 3], 0
005952E4  48 8D 45 67                     lea rax, [rbp + 0x67]
005952E8  48 8B 0D 01 0C 8D 00            mov rcx, qword ptr [rip + 0x8d0c01]
005952EF  48 8D 15 12 E0 A8 FF            lea rdx, [rip - 0x571fee]
005952F6  48 89 45 F7                     mov qword ptr [rbp - 9], rax
005952FA  45 33 C9                        xor r9d, r9d
005952FD  48 8D 45 F7                     lea rax, [rbp - 9]
00595301  C7 45 FF 04 00 00 00            mov dword ptr [rbp - 1], 4
00595308  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0059530D  45 33 C0                        xor r8d, r8d
00595310  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
00595318  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
0059531E  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00595324  E8 A7 9D CC FF                  call 0x14025f0d0
00595329  83 3D B8 1A 87 00 05            cmp dword ptr [rip + 0x871ab8], 5
00595330  76 78                           jbe 0x1405953aa
00595332  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
0059533C  48 8D 0D A5 1A 87 00            lea rcx, [rip + 0x871aa5]
00595343  E8 58 97 E9 FF                  call 0x14042eaa0
00595348  84 C0                           test al, al
0059534A  74 5E                           je 0x1405953aa
0059534C  83 65 33 00                     and dword ptr [rbp + 0x33], 0
00595350  48 8D 45 EF                     lea rax, [rbp - 0x11]
00595354  83 65 43 00                     and dword ptr [rbp + 0x43], 0
00595358  48 8D 15 A0 09 AB FF            lea rdx, [rip - 0x54f660]
0059535F  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
00595363  48 8D 0D 7E 1A 87 00            lea rcx, [rip + 0x871a7e]
0059536A  8B 45 67                        mov eax, dword ptr [rbp + 0x67]
0059536D  45 33 C9                        xor r9d, r9d
00595370  89 45 E7                        mov dword ptr [rbp - 0x19], eax
00595373  45 33 C0                        xor r8d, r8d
00595376  48 8D 45 E7                     lea rax, [rbp - 0x19]
0059537A  48 C7 45 EF 00 00 00 01         mov qword ptr [rbp - 0x11], 0x1000000
00595382  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
00595386  48 8D 45 07                     lea rax, [rbp + 7]
0059538A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0059538F  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
00595397  C7 45 2F 08 00 00 00            mov dword ptr [rbp + 0x2f], 8
0059539E  C7 45 3F 04 00 00 00            mov dword ptr [rbp + 0x3f], 4
005953A5  E8 36 0D E9 FF                  call 0x1404260e0
005953AA  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
005953AE  48 33 CC                        xor rcx, rsp
005953B1  E8 8A 72 11 00                  call 0x1406ac640
005953B6  48 81 C4 B0 00 00 00            add rsp, 0xb0
005953BD  5D                              pop rbp
005953BE  C3                              ret
005953BF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopDumpTraceLoadDumpStackFailure(int a1, __int64 a2, int a3, int a4)
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
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m5F;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 8868976)) ^ (v_rsp);
    v_stack_m18 = result;
    result = IopDumpIsTracingEnabled(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a1 = *(unsigned __int64 *)(v_rip + 9243649);
        a2 = v_rip - 5709806;
        v_stack_m68 = result;
        a4 = 0;
        result = v_stack_m68;
        v_stack_m60 = 4;
        v_stack_m80 = result;
        a3 = 0;
        v_stack_m88 = 1;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    if ((*(unsigned int *)(v_rip + 8854200)) <= 5) goto loc_005953AA;
    result = tlgKeywordOn(v_rip + 8854181, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m70;
        a2 = v_rip - 5568096;
        v_stack_m38 = result;
        a1 = v_rip + 8854142;
        result = v_stack_p8;
        a4 = 0;
        v_stack_m78 = (unsigned int)(result);
        a3 = 0;
        result = v_stack_m78;
        v_stack_m70 = 0x1000000ULL;
        v_stack_m28 = result;
        result = v_stack_m58;
        v_stack_m90 = result;
        v_stack_m98 = 4;
        v_stack_m30 = 8;
        v_stack_m20 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (176);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopDumpTraceLoadDumpStackFailure(int32_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
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
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m5F;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0x875470)) ^ (local_rsp);
    v_stack_m18 = result;
    result = IopDumpIsTracingEnabled(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg1 = *(uint64_t *)(v_rip + 0x8D0C01);
        Arg2 = v_rip - 5709806;
        v_stack_m68 = result;
        Arg4 = 0;
        result = v_stack_m68;
        v_stack_m60 = 4;
        v_stack_m80 = result;
        Arg3 = 0;
        v_stack_m88 = 1;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint32_t *)(v_rip + 0x871AB8)) <= 5) goto loc_005953AA;
    result = tlgKeywordOn(v_rip + 8854181, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m70;
        Arg2 = v_rip - 5568096;
        v_stack_m38 = result;
        Arg1 = v_rip + 8854142;
        result = v_stack_p8;
        Arg4 = 0;
        v_stack_m78 = (uint32_t)(result);
        Arg3 = 0;
        result = v_stack_m78;
        v_stack_m70 = 0x1000000ULL;
        v_stack_m28 = result;
        result = v_stack_m58;
        v_stack_m90 = result;
        v_stack_m98 = 4;
        v_stack_m30 = 8;
        v_stack_m20 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (176);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005952B8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005952B8[BB_005952B8]
  bb_005952E0[BB_005952E0]
  bb_00595329[BB_00595329]
  bb_00595332[BB_00595332]
  bb_0059534C[BB_0059534C]
  bb_005953AA[BB_005953AA]
  bb_005953BF[BB_005953BF]
  bb_005952B8 -->|branch| bb_00595329
  bb_005952B8 -->|fallthrough| bb_005952E0
  bb_005952E0 -->|flow| bb_00595329
  bb_00595329 -->|branch| bb_005953AA
  bb_00595329 -->|fallthrough| bb_00595332
  bb_00595332 -->|branch| bb_005953AA
  bb_00595332 -->|fallthrough| bb_0059534C
  bb_0059534C -->|flow| bb_005953AA
```
