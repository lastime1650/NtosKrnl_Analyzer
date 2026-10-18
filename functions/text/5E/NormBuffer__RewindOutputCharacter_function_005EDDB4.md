# NormBuffer__RewindOutputCharacter

- RVA: `0x005EDDB4`–`0x005EDDF1` (길이 `61` bytes)
- VA: `0x00000001405EDDB4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `18`개 명령, `61/61` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [Normalization__NormalizeCharacter](../../page/79/Normalization__NormalizeCharacter_function_00793D34.md) at `0x00793EB6`
- [Normalization__NormalizeCharacter](../../page/79/Normalization__NormalizeCharacter_function_00793D34.md) at `0x00793F29`
- [Normalization__NormalizeCharacter](../../page/79/Normalization__NormalizeCharacter_function_00793D34.md) at `0x00793F54`
- [Normalization__NormalizeCharacter](../../page/79/Normalization__NormalizeCharacter_function_00793D34.md) at `0x007942D6`
- [Normalization__NormalizeCharacter](../../page/79/Normalization__NormalizeCharacter_function_00793D34.md) at `0x00794477`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005EDDB4  4C 8B 41 28                     mov r8, qword ptr [rcx + 0x28]
005EDDB8  BA FF 23 00 00                  mov edx, 0x23ff
005EDDBD  49 8D 40 FE                     lea rax, [r8 - 2]
005EDDC1  66 03 10                        add dx, word ptr [rax]
005EDDC4  48 89 41 28                     mov qword ptr [rcx + 0x28], rax
005EDDC8  B8 FD 03 00 00                  mov eax, 0x3fd
005EDDCD  66 3B D0                        cmp dx, ax
005EDDD0  77 08                           ja 0x1405eddda
005EDDD2  49 8D 40 FC                     lea rax, [r8 - 4]
005EDDD6  48 89 41 28                     mov qword ptr [rcx + 0x28], rax
005EDDDA  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
005EDDDE  48 83 E8 02                     sub rax, 2
005EDDE2  48 89 41 40                     mov qword ptr [rcx + 0x40], rax
005EDDE6  33 C0                           xor eax, eax
005EDDE8  89 41 38                        mov dword ptr [rcx + 0x38], eax
005EDDEB  66 89 41 48                     mov word ptr [rcx + 0x48], ax
005EDDEF  C3                              ret
005EDDF0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NormBuffer__RewindOutputCharacter(__int64 a1)
{
    __int64 result;

    a2 = (unsigned __int16)(((unsigned int)(0x23FFULL)) + (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 40) - 2)));
    *(unsigned __int64 *)(a1 + 40) = *(unsigned __int64 *)(a1 + 40) - 2;
    result = (unsigned int)(0x3FDULL);
    if (((unsigned __int16)(a2)) <= ((unsigned __int16)((unsigned int)(0x3FDULL)))) {
        result = *(unsigned __int64 *)(a1 + 40) - 4;
        *(unsigned __int64 *)(a1 + 40) = result;
    }
    result = (*(unsigned __int64 *)(a1 + 24)) - (2);
    *(unsigned __int64 *)(a1 + 64) = result;
    result = 0;
    *(unsigned int *)(a1 + 56) = 0;
    *(unsigned __int16 *)(a1 + 72) = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NormBuffer__RewindOutputCharacter(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    a2 = (uint16_t)(((uint32_t)(0x23FFULL)) + (*(uint16_t *)(*(uint64_t *)(arg1 + 0x28) - 0x2)));
    *(uint64_t *)(arg1 + 0x28) = *(uint64_t *)(arg1 + 0x28) - 2;
    result = (uint32_t)(0x3FDULL);
    if (((uint16_t)(a2)) <= ((uint16_t)((uint32_t)(0x3FDULL)))) {
        result = *(uint64_t *)(arg1 + 0x28) - 4;
        *(uint64_t *)(arg1 + 0x28) = result;
    }
    result = (*(uint64_t *)(arg1 + 0x18)) - (2);
    *(uint64_t *)(arg1 + 0x40) = result;
    result = 0;
    *(uint32_t *)(arg1 + 0x38) = 0;
    *(uint16_t *)(arg1 + 0x48) = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg1` | `+ 0x38` | `32` | `W` |
| `Arg1` | `+ 0x40` | `64` | `W` |
| `Arg1` | `+ 0x48` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005EDDB4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005EDDB4[BB_005EDDB4]
  bb_005EDDD2[BB_005EDDD2]
  bb_005EDDDA[BB_005EDDDA]
  bb_005EDDF0[BB_005EDDF0]
  bb_005EDDB4 -->|branch| bb_005EDDDA
  bb_005EDDB4 -->|fallthrough| bb_005EDDD2
  bb_005EDDD2 -->|flow| bb_005EDDDA
```
