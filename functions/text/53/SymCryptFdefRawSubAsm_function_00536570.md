# SymCryptFdefRawSubAsm

- RVA: `0x00536570`–`0x005365BF` (길이 `79` bytes)
- VA: `0x0000000140536570`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C3108`
- 디코드: `22`개 명령, `79/79` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SymCryptFdefIntSubMixedSize](../52/SymCryptFdefIntSubMixedSize_function_0052D9D0.md) at `0x0052DA1A`
- [SymCryptFdefIntSubMixedSize](../52/SymCryptFdefIntSubMixedSize_function_0052D9D0.md) at `0x0052DA47`
- [SymCryptFdefIntSubSameSize](../52/SymCryptFdefIntSubSameSize_function_0052DAB8.md) at `0x0052DACC`
- [SymCryptFdefRawSub](../52/SymCryptFdefRawSub_function_0052E0BC.md) at `0x0052E0C0`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00536570  45 03 C9                        add r9d, r9d
00536573  48 33 C0                        xor rax, rax
00536576  48 8B 01                        mov rax, qword ptr [rcx]
00536579  48 1B 02                        sbb rax, qword ptr [rdx]
0053657C  49 89 00                        mov qword ptr [r8], rax
0053657F  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00536583  48 1B 42 08                     sbb rax, qword ptr [rdx + 8]
00536587  49 89 40 08                     mov qword ptr [r8 + 8], rax
0053658B  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
0053658F  48 1B 42 10                     sbb rax, qword ptr [rdx + 0x10]
00536593  49 89 40 10                     mov qword ptr [r8 + 0x10], rax
00536597  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0053659B  48 1B 42 18                     sbb rax, qword ptr [rdx + 0x18]
0053659F  49 89 40 18                     mov qword ptr [r8 + 0x18], rax
005365A3  48 8D 49 20                     lea rcx, [rcx + 0x20]
005365A7  48 8D 52 20                     lea rdx, [rdx + 0x20]
005365AB  4D 8D 40 20                     lea r8, [r8 + 0x20]
005365AF  41 FF C9                        dec r9d
005365B2  75 C2                           jne 0x140536576
005365B4  48 C7 C0 00 00 00 00            mov rax, 0
005365BB  48 13 C0                        adc rax, rax
005365BE  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdefRawSubAsm(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;

    a4 = (unsigned int)((a4) + (a4));
    result = 0;
loc_00536576:
    *(unsigned __int64 *)(a3) = *(unsigned __int64 *)(a1);
    *(unsigned __int64 *)(a3 + 8) = *(unsigned __int64 *)(a1 + 8);
    *(unsigned __int64 *)(a3 + 16) = *(unsigned __int64 *)(a1 + 16);
    *(unsigned __int64 *)(a3 + 24) = *(unsigned __int64 *)(a1 + 24);
    a4 = (unsigned int)((a4) - 1);
    if (condition_is_not_equal) goto loc_00536576;
    return 0;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdefRawSubAsm(void *Arg1, void *Arg2, void *Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    Arg4 = (uint32_t)((Arg4) + (Arg4));
    result = 0;
loc_00536576:
    *(uint64_t *)(arg3) = *(uint64_t *)(arg1);
    *(uint64_t *)(arg3 + 0x8) = *(uint64_t *)(arg1 + 0x8);
    *(uint64_t *)(arg3 + 0x10) = *(uint64_t *)(arg1 + 0x10);
    *(uint64_t *)(arg3 + 0x18) = *(uint64_t *)(arg1 + 0x18);
    Arg4 = (uint32_t)((Arg4) - 1);
    if (condition_is_not_equal) goto loc_00536576;
    return 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg3` | `+ 0x8` | `64` | `W` |
| `Arg3` | `+ 0x10` | `64` | `W` |
| `Arg3` | `+ 0x18` | `64` | `W` |
| `Arg3` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00536570&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00536570[BB_00536570]
  bb_00536576[BB_00536576]
  bb_005365B4[BB_005365B4]
  bb_00536570 -->|flow| bb_00536576
  bb_00536576 -->|branch| bb_00536576
  bb_00536576 -->|fallthrough| bb_005365B4
```
