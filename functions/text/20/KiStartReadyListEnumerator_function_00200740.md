# KiStartReadyListEnumerator

- RVA: `0x00200740`–`0x00200765` (길이 `37` bytes)
- VA: `0x0000000140200740`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `15`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiRemoveCurrentThreadScbReadyQueueEnumerator](KiRemoveCurrentThreadScbReadyQueueEnumerator_function_00201538.md) at `0x002015A8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00200740  33 C0                           xor eax, eax
00200742  89 11                           mov dword ptr [rcx], edx
00200744  4C 89 41 10                     mov qword ptr [rcx + 0x10], r8
00200748  85 D2                           test edx, edx
0020074A  74 15                           je 0x140200761
0020074C  0F BD D2                        bsr edx, edx
0020074F  8B C2                           mov eax, edx
00200751  48 C1 E0 04                     shl rax, 4
00200755  49 03 C0                        add rax, r8
00200758  88 51 04                        mov byte ptr [rcx + 4], dl
0020075B  48 89 41 08                     mov qword ptr [rcx + 8], rax
0020075F  C3                              ret
00200760  CC                              int3
00200761  B2 20                           mov dl, 0x20
00200763  EB F3                           jmp 0x140200758
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiStartReadyListEnumerator(__int64 a1, int a2, __int64 a3)
{
    __int64 result;

    result = 0;
    *(unsigned int *)(a1) = a2;
    *(unsigned __int64 *)(a1 + 16) = a3;
    if (a2 == 0) goto loc_00200761;
    result = ((unsigned int)(a2)) << (4);
    result = (result) + (a3);
loc_00200758:
    *(unsigned __int8 *)(a1 + 4) = (unsigned __int8)(a2);
    *(unsigned __int64 *)(a1 + 8) = result;
    return result;
loc_00200761:
    goto loc_00200758;
}
```

## 5. (Beta) C Style

```c
int64_t KiStartReadyListEnumerator(void *Arg1, int32_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = 0;
    *(uint32_t *)(arg1) = Arg2;
    *(uint64_t *)(arg1 + 0x10) = Arg3;
    if (Arg2 == 0) goto loc_00200761;
    result = ((uint32_t)(Arg2)) << (4);
    result = (result) + (Arg3);
loc_00200758:
    *(uint8_t *)(arg1 + 0x4) = (uint8_t)(Arg2);
    *(uint64_t *)(arg1 + 0x8) = result;
    return result;
loc_00200761:
    goto loc_00200758;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x4` | `8` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00200740&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00200740[BB_00200740]
  bb_0020074C[BB_0020074C]
  bb_00200758[BB_00200758]
  bb_00200760[BB_00200760]
  bb_00200761[BB_00200761]
  bb_00200740 -->|branch| bb_00200761
  bb_00200740 -->|fallthrough| bb_0020074C
  bb_0020074C -->|flow| bb_00200758
  bb_00200760 -->|flow| bb_00200761
  bb_00200761 -->|branch| bb_00200758
```
