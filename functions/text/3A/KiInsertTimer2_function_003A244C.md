# KiInsertTimer2

- RVA: `0x003A244C`–`0x003A24D8` (길이 `140` bytes)
- VA: `0x00000001403A244C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007132C`
- 디코드: `34`개 명령, `140/140` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x003A2470` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x003A2483` → [KiInsertTimer2WithCollectionLockHeld](KiInsertTimer2WithCollectionLockHeld_function_003A2CA0.md) (function, `0x003A2CA0`)
- `0x003A2491` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x003A24D1` → [KiHvEnlightenedGuestPriorityKick](../44/KiHvEnlightenedGuestPriorityKick_function_00443880.md) (function, `0x00443880`)

### Direct callers
- [sub_003A1A0C](Unknown_function_003A1A0C.md) at `0x003A1C19`
- [KiAdjustTimer2DueTimes](KiAdjustTimer2DueTimes_function_003A3550.md) at `0x003A36F2`

### Static image references
- `0x003A2463` → RVA `0x00FCF600` (`CACHEALI`; read)
- `0x003A24B0` → RVA `0x00F21FB0` (`.data`; read)
- `0x003A24B6` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x003A24CA` → RVA `0x00FC504C` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003A244C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003A2451  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
003A2456  57                              push rdi
003A2457  48 83 EC 20                     sub rsp, 0x20
003A245B  48 8B F1                        mov rsi, rcx
003A245E  C6 44 24 48 00                  mov byte ptr [rsp + 0x48], 0
003A2463  48 8D 0D 96 D1 C2 00            lea rcx, [rip + 0xc2d196]
003A246A  49 8B D8                        mov rbx, r8
003A246D  40 8A FA                        mov dil, dl
003A2470  E8 BB 5F E6 FF                  call 0x140208430
003A2475  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
003A247A  4C 8B C3                        mov r8, rbx
003A247D  40 8A D7                        mov dl, dil
003A2480  48 8B CE                        mov rcx, rsi
003A2483  E8 18 08 00 00                  call 0x1403a2ca0
003A2488  48 8D 0D 71 D1 C2 00            lea rcx, [rip + 0xc2d171]
003A248F  8A D8                           mov bl, al
003A2491  E8 DA 41 E6 FF                  call 0x140206670
003A2496  80 7C 24 48 00                  cmp byte ptr [rsp + 0x48], 0
003A249B  75 13                           jne 0x1403a24b0
003A249D  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
003A24A2  8A C3                           mov al, bl
003A24A4  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
003A24A9  48 83 C4 20                     add rsp, 0x20
003A24AD  5F                              pop rdi
003A24AE  C3                              ret
003A24AF  CC                              int3
003A24B0  8B 0D FA FA B7 00               mov ecx, dword ptr [rip + 0xb7fafa]
003A24B6  48 8D 15 83 67 C2 00            lea rdx, [rip + 0xc26783]
003A24BD  48 8B 14 CA                     mov rdx, qword ptr [rdx + rcx*8]
003A24C1  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
003A24CA  44 8B 05 7B 2B C2 00            mov r8d, dword ptr [rip + 0xc22b7b]
003A24D1  E8 AA 13 0A 00                  call 0x140443880
003A24D6  EB C5                           jmp 0x1403a249d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiInsertTimer2(__int64 a1, unsigned __int8 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_stack_p20 = 0;
    result = KeAcquireSpinLockAtDpcLevel(v_rip + 12767638, a2, a3, a4);
    result = KiInsertTimer2WithCollectionLockHeld(a1, a2, a3, v_stack_p20);
    result = KxReleaseSpinLock(v_rip + 12767601, a2, a3, v_stack_p20);
    if (v_stack_p20 != 0) goto loc_003A24B0;
loc_003A249D:
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)((unsigned __int8)(result));
loc_003A24B0:
    result = KiHvEnlightenedGuestPriorityKick(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(v_rip + 12740483 + (unsigned int)(*(unsigned int *)(v_rip + 12057338)) * 8), (unsigned int)(*(unsigned int *)(v_rip + 12725115)), v_stack_p20);
    goto loc_003A249D;
}
```

## 5. (Beta) C Style

```c
int64_t KiInsertTimer2(int64_t Arg1, uint8_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint8_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    v_stack_p20 = 0;
    result = KeAcquireSpinLockAtDpcLevel(v_rip + 12767638, Arg2, Arg3, a4);
    result = KiInsertTimer2WithCollectionLockHeld(Arg1, Arg2, Arg3, v_stack_p20);
    result = KxReleaseSpinLock(v_rip + 12767601, Arg2, Arg3, v_stack_p20);
    if (v_stack_p20 != 0) goto loc_003A24B0;
loc_003A249D:
    local_rsp = (local_rsp) + (32);
    return (uint8_t)((uint8_t)(result));
loc_003A24B0:
    result = KiHvEnlightenedGuestPriorityKick(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(v_rip + 0xC26783 + (uint32_t)(*(uint32_t *)(v_rip + 0xB7FAFA)) * 8), (uint32_t)(*(uint32_t *)(v_rip + 0xC22B7B)), v_stack_p20);
    goto loc_003A249D;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003A244C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003A244C[BB_003A244C]
  bb_003A249D[BB_003A249D]
  bb_003A24AF[BB_003A24AF]
  bb_003A24B0[BB_003A24B0]
  bb_003A244C -->|branch| bb_003A24B0
  bb_003A244C -->|fallthrough| bb_003A249D
  bb_003A24AF -->|flow| bb_003A24B0
  bb_003A24B0 -->|branch| bb_003A249D
```
