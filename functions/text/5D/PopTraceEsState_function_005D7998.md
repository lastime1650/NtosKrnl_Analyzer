# PopTraceEsState

- RVA: `0x005D7998`–`0x005D7B07` (길이 `367` bytes)
- VA: `0x00000001405D7998`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CC6F8`
- 디코드: `71`개 명령, `367/367` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x005D79D5` → [tlgKeywordOn](../42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x005D7AEC` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x005D7AF8` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopEsSnapTelemetry](../../page/70/PopEsSnapTelemetry_function_00700BC0.md) at `0x00700C6E`

### Static image references
- `0x005D79A6` → RVA `0x00E0A740` (`.data`; read)
- `0x005D79B4` → RVA `0x00E07748` (`.data`; read)
- `0x005D79E2` → RVA `0x00E67A08` (`.data`; read)
- `0x005D79E8` → RVA `0x0004A27E` (`.rdata`; read)
- `0x005D7A2D` → RVA `0x00E67A1C` (`.data`; read)
- `0x005D7A51` → RVA `0x00E67A20` (`.data`; read)
- `0x005D7A64` → RVA `0x00E67A00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D7998  40 55                           push rbp
005D799A  48 8D 6C 24 E0                  lea rbp, [rsp - 0x20]
005D799F  48 81 EC 20 01 00 00            sub rsp, 0x120
005D79A6  48 8B 05 93 2D 83 00            mov rax, qword ptr [rip + 0x832d93]
005D79AD  48 33 C4                        xor rax, rsp
005D79B0  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
005D79B4  83 3D 8D FD 82 00 05            cmp dword ptr [rip + 0x82fd8d], 5
005D79BB  4C 8B CA                        mov r9, rdx
005D79BE  0F 86 2D 01 00 00               jbe 0x1405d7af1
005D79C4  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
005D79CE  48 8D 0D 73 FD 82 00            lea rcx, [rip + 0x82fd73]
005D79D5  E8 C6 70 E5 FF                  call 0x14042eaa0
005D79DA  84 C0                           test al, al
005D79DC  0F 84 0F 01 00 00               je 0x1405d7af1
005D79E2  8B 05 20 00 89 00               mov eax, dword ptr [rip + 0x890020]
005D79E8  48 8D 15 8F 28 A7 FF            lea rdx, [rip - 0x58d771]
005D79EF  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
005D79F3  48 8D 0D 4E FD 82 00            lea rcx, [rip + 0x82fd4e]
005D79FA  48 8D 44 24 30                  lea rax, [rsp + 0x30]
005D79FF  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
005D7A04  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
005D7A08  45 33 C9                        xor r9d, r9d
005D7A0B  48 8D 44 24 50                  lea rax, [rsp + 0x50]
005D7A10  44 89 44 24 34                  mov dword ptr [rsp + 0x34], r8d
005D7A15  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
005D7A19  45 33 C0                        xor r8d, r8d
005D7A1C  48 8D 44 24 34                  lea rax, [rsp + 0x34]
005D7A21  48 C7 45 88 04 00 00 00         mov qword ptr [rbp - 0x78], 4
005D7A29  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
005D7A2D  0F B6 05 E8 FF 88 00            movzx eax, byte ptr [rip + 0x88ffe8]
005D7A34  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
005D7A38  48 8D 44 24 38                  lea rax, [rsp + 0x38]
005D7A3D  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
005D7A41  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
005D7A44  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
005D7A48  48 8D 44 24 3C                  lea rax, [rsp + 0x3c]
005D7A4D  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
005D7A51  8B 05 C9 FF 88 00               mov eax, dword ptr [rip + 0x88ffc9]
005D7A57  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
005D7A5B  48 8D 44 24 40                  lea rax, [rsp + 0x40]
005D7A60  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
005D7A64  0F B6 05 95 FF 88 00            movzx eax, byte ptr [rip + 0x88ff95]
005D7A6B  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
005D7A6F  48 8D 44 24 44                  lea rax, [rsp + 0x44]
005D7A74  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
005D7A78  8B 45 68                        mov eax, dword ptr [rbp + 0x68]
005D7A7B  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
005D7A7F  48 8D 44 24 48                  lea rax, [rsp + 0x48]
005D7A84  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
005D7A88  48 8D 44 24 58                  lea rax, [rsp + 0x58]
005D7A8D  48 89 45 00                     mov qword ptr [rbp], rax
005D7A91  48 8D 44 24 60                  lea rax, [rsp + 0x60]
005D7A96  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005D7A9B  C7 44 24 20 0B 00 00 00         mov dword ptr [rsp + 0x20], 0xb
005D7AA3  48 C7 45 98 08 00 00 00         mov qword ptr [rbp - 0x68], 8
005D7AAB  48 C7 45 A8 04 00 00 00         mov qword ptr [rbp - 0x58], 4
005D7AB3  48 C7 45 B8 04 00 00 00         mov qword ptr [rbp - 0x48], 4
005D7ABB  48 C7 45 C8 04 00 00 00         mov qword ptr [rbp - 0x38], 4
005D7AC3  48 C7 45 D8 04 00 00 00         mov qword ptr [rbp - 0x28], 4
005D7ACB  48 C7 45 E8 04 00 00 00         mov qword ptr [rbp - 0x18], 4
005D7AD3  48 C7 45 F8 04 00 00 00         mov qword ptr [rbp - 8], 4
005D7ADB  48 C7 44 24 58 00 00 00 01      mov qword ptr [rsp + 0x58], 0x1000000
005D7AE4  48 C7 45 08 08 00 00 00         mov qword ptr [rbp + 8], 8
005D7AEC  E8 EF E5 E4 FF                  call 0x1404260e0
005D7AF1  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
005D7AF5  48 33 CC                        xor rcx, rsp
005D7AF8  E8 43 4B 0D 00                  call 0x1406ac640
005D7AFD  48 81 C4 20 01 00 00            add rsp, 0x120
005D7B04  5D                              pop rbp
005D7B05  C3                              ret
005D7B06  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopTraceEsState(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned int a5, __int64 a6, __int64 a7, unsigned int a8)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned int v_stack_mE8;
    unsigned int v_stack_mEC;
    unsigned int v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned int v_stack_mF8;

    v_rsp = (v_rsp) - (288);
    result = (*(unsigned __int64 *)(v_rip + 8596883)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 8584589)) <= 5) goto loc_005D7AF1;
    result = tlgKeywordOn(v_rip + 8584563, a2, a3, a2);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned int *)(v_rip + 8978464);
        a2 = v_rip - 5822321;
        v_stack_mF8 = (unsigned int)(result);
        a1 = v_rip + 8584526;
        result = v_stack_mF8;
        v_stack_mD8 = a2;
        v_stack_mA8 = result;
        a4 = 0;
        result = v_stack_mD8;
        v_stack_mF4 = a3;
        v_stack_m98 = result;
        a3 = 0;
        result = v_stack_mF4;
        v_stack_mA0 = 4;
        v_stack_m88 = result;
        result = *(unsigned __int8 *)(v_rip + 8978408);
        v_stack_mF0 = (unsigned int)(result);
        result = v_stack_mF0;
        v_stack_m78 = result;
        result = a5;
        v_stack_mEC = (unsigned int)(result);
        result = v_stack_mEC;
        v_stack_m68 = result;
        result = *(unsigned int *)(v_rip + 8978377);
        v_stack_mE8 = (unsigned int)(result);
        result = v_stack_mE8;
        v_stack_m58 = result;
        result = *(unsigned __int8 *)(v_rip + 8978325);
        v_stack_mE4 = (unsigned int)(result);
        result = v_stack_mE4;
        v_stack_m48 = result;
        result = a8;
        v_stack_mE0 = (unsigned int)(result);
        result = v_stack_mE0;
        v_stack_m38 = result;
        result = v_stack_mD0;
        v_stack_m28 = result;
        result = v_stack_mC8;
        v_stack_m100 = result;
        v_stack_m108 = 11;
        v_stack_m90 = 8;
        v_stack_m80 = 4;
        v_stack_m70 = 4;
        v_stack_m60 = 4;
        v_stack_m50 = 4;
        v_stack_m40 = 4;
        v_stack_m30 = 4;
        v_stack_mD0 = 0x1000000ULL;
        v_stack_m20 = 8;
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
int64_t PopTraceEsState(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, uint64_t Arg6, uint64_t Arg7, uint32_t Arg8)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m108;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint32_t v_stack_mE8;
    uint32_t v_stack_mEC;
    uint32_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint32_t v_stack_mF8;

    local_rsp = (local_rsp) - (288);
    result = (*(uint64_t *)(v_rip + 0x832D93)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x82FD8D)) <= 5) goto loc_005D7AF1;
    result = tlgKeywordOn(v_rip + 8584563, Arg2, Arg3, Arg2);
    if ((uint8_t)(result) != 0) {
        result = *(uint32_t *)(v_rip + 0x890020);
        Arg2 = v_rip - 5822321;
        v_stack_mF8 = (uint32_t)(result);
        Arg1 = v_rip + 8584526;
        result = v_stack_mF8;
        v_stack_mD8 = Arg2;
        v_stack_mA8 = result;
        Arg4 = 0;
        result = v_stack_mD8;
        v_stack_mF4 = Arg3;
        v_stack_m98 = result;
        Arg3 = 0;
        result = v_stack_mF4;
        v_stack_mA0 = 4;
        v_stack_m88 = result;
        result = *(uint8_t *)(v_rip + 0x88FFE8);
        v_stack_mF0 = (uint32_t)(result);
        result = v_stack_mF0;
        v_stack_m78 = result;
        result = Arg5;
        v_stack_mEC = (uint32_t)(result);
        result = v_stack_mEC;
        v_stack_m68 = result;
        result = *(uint32_t *)(v_rip + 0x88FFC9);
        v_stack_mE8 = (uint32_t)(result);
        result = v_stack_mE8;
        v_stack_m58 = result;
        result = *(uint8_t *)(v_rip + 0x88FF95);
        v_stack_mE4 = (uint32_t)(result);
        result = v_stack_mE4;
        v_stack_m48 = result;
        result = Arg8;
        v_stack_mE0 = (uint32_t)(result);
        result = v_stack_mE0;
        v_stack_m38 = result;
        result = v_stack_mD0;
        v_stack_m28 = result;
        result = v_stack_mC8;
        v_stack_m100 = result;
        v_stack_m108 = 11;
        v_stack_m90 = 8;
        v_stack_m80 = 4;
        v_stack_m70 = 4;
        v_stack_m60 = 4;
        v_stack_m50 = 4;
        v_stack_m40 = 4;
        v_stack_m30 = 4;
        v_stack_mD0 = 0x1000000ULL;
        v_stack_m20 = 8;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (288);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D7998&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D7998[BB_005D7998]
  bb_005D79C4[BB_005D79C4]
  bb_005D79E2[BB_005D79E2]
  bb_005D7AF1[BB_005D7AF1]
  bb_005D7B06[BB_005D7B06]
  bb_005D7998 -->|branch| bb_005D7AF1
  bb_005D7998 -->|fallthrough| bb_005D79C4
  bb_005D79C4 -->|branch| bb_005D7AF1
  bb_005D79C4 -->|fallthrough| bb_005D79E2
  bb_005D79E2 -->|flow| bb_005D7AF1
```
