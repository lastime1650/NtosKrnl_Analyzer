# SymCryptFdef369RawSubAsm

- RVA: `0x0053B520`–`0x0053B563` (길이 `67` bytes)
- VA: `0x000000014053B520`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C3108`
- 디코드: `19`개 명령, `67/67` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SymCryptFdef369ModAddGeneric](SymCryptFdef369ModAddGeneric_function_005373C0.md) at `0x00537428`
- [SymCryptFdef369ModSubGeneric](SymCryptFdef369ModSubGeneric_function_005376C0.md) at `0x0053770F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0053B520  41 FF C1                        inc r9d
0053B523  48 33 C0                        xor rax, rax
0053B526  48 8B 01                        mov rax, qword ptr [rcx]
0053B529  48 1B 02                        sbb rax, qword ptr [rdx]
0053B52C  49 89 00                        mov qword ptr [r8], rax
0053B52F  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0053B533  48 1B 42 08                     sbb rax, qword ptr [rdx + 8]
0053B537  49 89 40 08                     mov qword ptr [r8 + 8], rax
0053B53B  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
0053B53F  48 1B 42 10                     sbb rax, qword ptr [rdx + 0x10]
0053B543  49 89 40 10                     mov qword ptr [r8 + 0x10], rax
0053B547  48 8D 49 18                     lea rcx, [rcx + 0x18]
0053B54B  48 8D 52 18                     lea rdx, [rdx + 0x18]
0053B54F  4D 8D 40 18                     lea r8, [r8 + 0x18]
0053B553  41 FF C9                        dec r9d
0053B556  75 CE                           jne 0x14053b526
0053B558  48 C7 C0 00 00 00 00            mov rax, 0
0053B55F  48 13 C0                        adc rax, rax
0053B562  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdef369RawSubAsm(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;

    a4 = (unsigned int)((a4) + 1);
    result = 0;
loc_0053B526:
    *(unsigned __int64 *)(a3) = *(unsigned __int64 *)(a1);
    *(unsigned __int64 *)(a3 + 8) = *(unsigned __int64 *)(a1 + 8);
    *(unsigned __int64 *)(a3 + 16) = *(unsigned __int64 *)(a1 + 16);
    a4 = (unsigned int)((a4) - 1);
    if (condition_is_not_equal) goto loc_0053B526;
    return 0;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdef369RawSubAsm(void *Arg1, void *Arg2, void *Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    Arg4 = (uint32_t)((Arg4) + 1);
    result = 0;
loc_0053B526:
    *(uint64_t *)(arg3) = *(uint64_t *)(arg1);
    *(uint64_t *)(arg3 + 0x8) = *(uint64_t *)(arg1 + 0x8);
    *(uint64_t *)(arg3 + 0x10) = *(uint64_t *)(arg1 + 0x10);
    Arg4 = (uint32_t)((Arg4) - 1);
    if (condition_is_not_equal) goto loc_0053B526;
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
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg3` | `+ 0x8` | `64` | `W` |
| `Arg3` | `+ 0x10` | `64` | `W` |
| `Arg3` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0053B520&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0053B520[BB_0053B520]
  bb_0053B526[BB_0053B526]
  bb_0053B558[BB_0053B558]
  bb_0053B520 -->|flow| bb_0053B526
  bb_0053B526 -->|branch| bb_0053B526
  bb_0053B526 -->|fallthrough| bb_0053B558
```
