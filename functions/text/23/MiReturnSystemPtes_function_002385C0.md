# MiReturnSystemPtes

- RVA: `0x002385C0`–`0x00238654` (길이 `148` bytes)
- VA: `0x00000001402385C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060A68`
- 디코드: `42`개 명령, `148/148` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00238634` → [MiReturnSystemVa](MiReturnSystemVa_function_002394C4.md) (function, `0x002394C4`)

### Direct callers
- [sub_00237DE0](Unknown_function_00237DE0.md) at `0x0023829D`
- [MiReleasePtes](../24/MiReleasePtes_function_00247240.md) at `0x002478FD`
- [MiAttemptCoalesce](../47/MiAttemptCoalesce_function_00479EB0.md) at `0x00479FAD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002385C0  40 53                           push rbx
002385C2  48 83 EC 20                     sub rsp, 0x20
002385C6  8B 41 28                        mov eax, dword ptr [rcx + 0x28]
002385C9  4C 8B D1                        mov r10, rcx
002385CC  49 8B D9                        mov rbx, r9
002385CF  49 8B C8                        mov rcx, r8
002385D2  48 C1 E3 04                     shl rbx, 4
002385D6  44 8B DA                        mov r11d, edx
002385D9  0F BA E0 00                     bt eax, 0
002385DD  49 0F 43 D9                     cmovae rbx, r9
002385E1  48 C1 E1 04                     shl rcx, 4
002385E5  0F BA E0 00                     bt eax, 0
002385E9  49 8B 42 20                     mov rax, qword ptr [r10 + 0x20]
002385ED  49 0F 43 C8                     cmovae rcx, r8
002385F1  48 8D 14 C8                     lea rdx, [rax + rcx*8]
002385F5  48 8B C3                        mov rax, rbx
002385F8  48 F7 D8                        neg rax
002385FB  F0 49 01 42 38                  lock add qword ptr [r10 + 0x38], rax
00238600  48 C1 E2 19                     shl rdx, 0x19
00238604  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0023860E  45 8B 42 2C                     mov r8d, dword ptr [r10 + 0x2c]
00238612  48 C1 E3 1C                     shl rbx, 0x1c
00238616  48 C1 E0 19                     shl rax, 0x19
0023861A  48 2B D0                        sub rdx, rax
0023861D  48 03 DA                        add rbx, rdx
00238620  48 8B CA                        mov rcx, rdx
00238623  48 C1 F9 10                     sar rcx, 0x10
00238627  48 C1 FB 10                     sar rbx, 0x10
0023862B  41 83 FB 01                     cmp r11d, 1
0023862F  74 0F                           je 0x140238640
00238631  48 8B D3                        mov rdx, rbx
00238634  E8 8B 0E 00 00                  call 0x1402394c4
00238639  48 83 C4 20                     add rsp, 0x20
0023863D  5B                              pop rbx
0023863E  C3                              ret
0023863F  CC                              int3
00238640  B8 0A 00 00 00                  mov eax, 0xa
00238645  41 83 F8 08                     cmp r8d, 8
00238649  8D 50 02                        lea edx, [rax + 2]
0023864C  0F 44 C2                        cmove eax, edx
0023864F  44 8B C0                        mov r8d, eax
00238652  EB DD                           jmp 0x140238631
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReturnSystemPtes(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    v_rbx = (a4) << (4);
    if (condition_is_above_or_equal) { v_rbx = a4; }
    a1 = (a3) << (4);
    if (condition_is_above_or_equal) { a1 = a3; }
    result = -(v_rbx);
    a2 = (*(unsigned __int64 *)(a1 + 32) + a1 * 8) << (25);
    v_rbx = (v_rbx) << (28);
    result = (result) << (25);
    a2 = (a2) - (result);
    v_rbx = (v_rbx) + (a2);
    a1 = (a2) >> (16);
    v_rbx = (v_rbx) >> (16);
    if (((unsigned int)((unsigned int)(a2))) == 1) goto loc_00238640;
loc_00238631:
    result = MiReturnSystemVa(a1, v_rbx, (unsigned int)(*(unsigned int *)(a1 + 44)), a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_00238640:
    result = 10;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 44)))) == 8) { result = (unsigned int)(10 + 2); }
    goto loc_00238631;
}
```

## 5. (Beta) C Style

```c
int64_t MiReturnSystemPtes(void *Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    local_rbx = (Arg4) << (4);
    if (condition_is_above_or_equal) { local_rbx = Arg4; }
    Arg1 = (Arg3) << (4);
    if (condition_is_above_or_equal) { Arg1 = Arg3; }
    result = -(local_rbx);
    Arg2 = (*(uint64_t *)(arg1 + 0x20) + Arg1 * 8) << (25);
    local_rbx = (local_rbx) << (28);
    result = (result) << (25);
    Arg2 = (Arg2) - (result);
    local_rbx = (local_rbx) + (Arg2);
    Arg1 = (Arg2) >> (16);
    local_rbx = (local_rbx) >> (16);
    if (((uint32_t)((uint32_t)(Arg2))) == 1) goto loc_00238640;
loc_00238631:
    result = MiReturnSystemVa(Arg1, local_rbx, (uint32_t)(*(uint32_t *)(arg1 + 0x2C)), Arg4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_00238640:
    result = 10;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C)))) == 8) { result = (uint32_t)(10 + 2); }
    goto loc_00238631;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x2C` | `32` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002385C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002385C0[BB_002385C0]
  bb_00238631[BB_00238631]
  bb_0023863F[BB_0023863F]
  bb_00238640[BB_00238640]
  bb_002385C0 -->|branch| bb_00238640
  bb_002385C0 -->|fallthrough| bb_00238631
  bb_0023863F -->|flow| bb_00238640
  bb_00238640 -->|branch| bb_00238631
```
