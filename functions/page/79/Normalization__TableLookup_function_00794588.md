# Normalization__TableLookup

- RVA: `0x00794588`–`0x007945A5` (길이 `29` bytes)
- VA: `0x0000000140794588`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [NormBuffer__GetLastChar](../../text/5E/NormBuffer__GetLastChar_function_005ED8F8.md) at `0x005ED95A`
- [NormBuffer__IsBlocked](../../text/5E/NormBuffer__IsBlocked_function_005EDA7C.md) at `0x005EDAC3`
- [NormBuffer__SortBeforeSameClass](../../text/5E/NormBuffer__SortBeforeSameClass_function_005EDDF8.md) at `0x005EDE65`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00794588  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
0079458C  44 8B CA                        mov r9d, edx
0079458F  41 0F B6 D0                     movzx edx, r8b
00794593  41 83 E1 7F                     and r9d, 0x7f
00794597  48 C1 E2 07                     shl rdx, 7
0079459B  4C 03 CA                        add r9, rdx
0079459E  41 8A 44 01 80                  mov al, byte ptr [r9 + rax - 0x80]
007945A3  C3                              ret
007945A4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Normalization__TableLookup(__int64 a1, int a2, unsigned __int8 a3)
{
    a4 = (unsigned int)(((unsigned int)(a2)) & (127));
    a2 = (a3) << (7);
    a4 = (a4) + (a2);
    return *(unsigned __int8 *)(a4 + *(unsigned __int64 *)(a1 + 40) * 1 - 128);
}
```

## 5. (Beta) C Style

```c
int64_t Normalization__TableLookup(void *Arg1, void *Arg2, uint8_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    a4 = (uint32_t)(((uint32_t)(Arg2)) & (127));
    Arg2 = (Arg3) << (7);
    a4 = (a4) + (Arg2);
    return *(uint8_t *)(a4 + *(uint64_t *)(arg1 + 0x28) * 1 - 0x80);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg2` | `- 0x80 + rax*1` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00794588&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00794588[BB_00794588]
  bb_007945A4[BB_007945A4]
```
