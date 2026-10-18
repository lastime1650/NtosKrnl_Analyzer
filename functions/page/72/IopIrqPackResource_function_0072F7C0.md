# IopIrqPackResource

- RVA: `0x0072F7C0`–`0x0072F7EF` (길이 `47` bytes)
- VA: `0x000000014072F7C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `13`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0072F7C0  41 C6 00 02                     mov byte ptr [r8], 2
0072F7C4  0F B7 41 04                     movzx eax, word ptr [rcx + 4]
0072F7C8  66 41 89 40 02                  mov word ptr [r8 + 2], ax
0072F7CD  8A 41 02                        mov al, byte ptr [rcx + 2]
0072F7D0  41 88 40 01                     mov byte ptr [r8 + 1], al
0072F7D4  B8 FF FF FF FF                  mov eax, 0xffffffff
0072F7D9  49 89 40 0C                     mov qword ptr [r8 + 0xc], rax
0072F7DD  33 C0                           xor eax, eax
0072F7DF  66 41 89 40 06                  mov word ptr [r8 + 6], ax
0072F7E4  41 89 50 08                     mov dword ptr [r8 + 8], edx
0072F7E8  66 41 89 50 04                  mov word ptr [r8 + 4], dx
0072F7ED  C3                              ret
0072F7EE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopIrqPackResource(__int64 a1, int a2, __int64 a3)
{
    __int64 result;

    *(unsigned __int8 *)(a3) = 2;
    *(unsigned __int16 *)(a3 + 2) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 4));
    *(unsigned __int8 *)(a3 + 1) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 2));
    *(unsigned __int64 *)(a3 + 12) = (unsigned int)(0xFFFFFFFFULL);
    result = 0;
    *(unsigned __int16 *)(a3 + 6) = 0;
    *(unsigned int *)(a3 + 8) = a2;
    *(unsigned __int16 *)(a3 + 4) = (unsigned __int16)(a2);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopIrqPackResource(void *Arg1, int32_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    *(uint8_t *)(arg3) = 2;
    *(uint16_t *)(arg3 + 0x2) = (uint16_t)(*(uint16_t *)(arg1 + 0x4));
    *(uint8_t *)(arg3 + 0x1) = (uint8_t)(*(uint8_t *)(arg1 + 0x2));
    *(uint64_t *)(arg3 + 0xC) = (uint32_t)(0xFFFFFFFFULL);
    result = 0;
    *(uint16_t *)(arg3 + 0x6) = 0;
    *(uint32_t *)(arg3 + 0x8) = Arg2;
    *(uint16_t *)(arg3 + 0x4) = (uint16_t)(Arg2);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2` | `8` | `R` |
| `Arg1` | `+ 0x4` | `16` | `R` |
| `Arg3` | `+ 0x0` | `8` | `W` |
| `Arg3` | `+ 0x1` | `8` | `W` |
| `Arg3` | `+ 0x2` | `16` | `W` |
| `Arg3` | `+ 0x4` | `16` | `W` |
| `Arg3` | `+ 0x6` | `16` | `W` |
| `Arg3` | `+ 0x8` | `32` | `W` |
| `Arg3` | `+ 0xC` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0072F7C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0072F7C0[BB_0072F7C0]
  bb_0072F7EE[BB_0072F7EE]
```
