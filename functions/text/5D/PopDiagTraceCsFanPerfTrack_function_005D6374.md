# PopDiagTraceCsFanPerfTrack

- RVA: `0x005D6374`–`0x005D642A` (길이 `182` bytes)
- VA: `0x00000001405D6374`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AD3B0`
- 디코드: `38`개 명령, `182/182` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x005D63A6` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x005D6412` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x005D641F` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopFanEndCsFanPeriod](../../page/76/PopFanEndCsFanPeriod_function_00769158.md) at `0x007691B3`

### Static image references
- `0x005D6380` → RVA `0x00E0A740` (`.data`; read)
- `0x005D638F` → RVA `0x00E67858` (`.data`; read)
- `0x005D6398` → RVA `0x00F0B408` (`.data`; read)
- `0x005D639F` → RVA `0x00021770` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D6374  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
005D6378  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
005D637C  48 83 EC 78                     sub rsp, 0x78
005D6380  48 8B 05 B9 43 83 00            mov rax, qword ptr [rip + 0x8343b9]
005D6387  48 33 C4                        xor rax, rsp
005D638A  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
005D638F  80 3D C2 14 89 00 00            cmp byte ptr [rip + 0x8914c2], 0
005D6396  74 7F                           je 0x1405d6417
005D6398  48 8B 0D 69 50 93 00            mov rcx, qword ptr [rip + 0x935069]
005D639F  48 8D 15 CA B3 A4 FF            lea rdx, [rip - 0x5b4c36]
005D63A6  E8 A5 C0 DB FF                  call 0x140392450
005D63AB  84 C0                           test al, al
005D63AD  74 68                           je 0x1405d6417
005D63AF  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
005D63B4  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
005D63BC  83 64 24 5C 00                  and dword ptr [rsp + 0x5c], 0
005D63C1  48 8D 15 A8 B3 A4 FF            lea rdx, [rip - 0x5b4c58]
005D63C8  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
005D63CD  B9 04 00 00 00                  mov ecx, 4
005D63D2  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
005D63DA  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
005D63DE  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
005D63E3  45 33 C9                        xor r9d, r9d
005D63E6  48 8D 44 24 40                  lea rax, [rsp + 0x40]
005D63EB  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
005D63EF  48 8B 0D 12 50 93 00            mov rcx, qword ptr [rip + 0x935012]
005D63F6  45 33 C0                        xor r8d, r8d
005D63F9  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005D63FE  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
005D6406  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005D640C  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005D6412  E8 B9 8C C8 FF                  call 0x14025f0d0
005D6417  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
005D641C  48 33 CC                        xor rcx, rsp
005D641F  E8 1C 62 0D 00                  call 0x1406ac640
005D6424  48 83 C4 78                     add rsp, 0x78
005D6428  C3                              ret
005D6429  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceCsFanPerfTrack(int a1, int a2, int a3, int a4)
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
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_p10;
    unsigned int v_stack_p8;

    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (120);
    result = (*(unsigned __int64 *)(v_rip + 8602553)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 8983746)) == 0) goto loc_005D6417;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 9654377), v_rip - 5983286, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a2 = v_rip - 5983320;
        v_stack_m38 = result;
        a1 = 4;
        result = v_stack_p10;
        v_stack_m30 = a1;
        v_stack_m28 = result;
        a4 = 0;
        result = v_stack_m38;
        v_stack_m20 = a1;
        a1 = *(unsigned __int64 *)(v_rip + 9654290);
        a3 = 0;
        v_stack_m40 = result;
        v_stack_m48 = 2;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (120);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceCsFanPerfTrack(int32_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
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
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_p10;
    uint32_t v_stack_p8;

    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (120);
    result = (*(uint64_t *)(v_rip + 0x8343B9)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0x8914C2)) == 0) goto loc_005D6417;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x935069), v_rip - 5983286, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg2 = v_rip - 5983320;
        v_stack_m38 = result;
        Arg1 = 4;
        result = v_stack_p10;
        v_stack_m30 = Arg1;
        v_stack_m28 = result;
        Arg4 = 0;
        result = v_stack_m38;
        v_stack_m20 = Arg1;
        Arg1 = *(uint64_t *)(v_rip + 0x935012);
        Arg3 = 0;
        v_stack_m40 = result;
        v_stack_m48 = 2;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (120);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D6374&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D6374[BB_005D6374]
  bb_005D6398[BB_005D6398]
  bb_005D63AF[BB_005D63AF]
  bb_005D6417[BB_005D6417]
  bb_005D6429[BB_005D6429]
  bb_005D6374 -->|branch| bb_005D6417
  bb_005D6374 -->|fallthrough| bb_005D6398
  bb_005D6398 -->|branch| bb_005D6417
  bb_005D6398 -->|fallthrough| bb_005D63AF
  bb_005D63AF -->|flow| bb_005D6417
```
