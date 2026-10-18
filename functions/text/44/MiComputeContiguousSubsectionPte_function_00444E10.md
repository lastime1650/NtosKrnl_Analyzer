# MiComputeContiguousSubsectionPte

- RVA: `0x00444E10`–`0x00444E33` (길이 `35` bytes)
- VA: `0x0000000140444E10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_006DAEBA](../6D/Unknown_function_006DAEBA.md) at `0x006DAF11`
- [sub_00884EE1](../../page/88/Unknown_function_00884EE1.md) at `0x008851A1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00444E10  8B 41 2C                        mov eax, dword ptr [rcx + 0x2c]
00444E13  44 8B 41 34                     mov r8d, dword ptr [rcx + 0x34]
00444E17  41 81 E0 FF FF FF 3F            and r8d, 0x3fffffff
00444E1E  41 2B C0                        sub eax, r8d
00444E21  48 3B D0                        cmp rdx, rax
00444E24  72 03                           jb 0x140444e29
00444E26  8D 50 FF                        lea edx, [rax - 1]
00444E29  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00444E2D  48 8D 04 D0                     lea rax, [rax + rdx*8]
00444E31  C3                              ret
00444E32  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiComputeContiguousSubsectionPte(__int64 a1, __int64 a2)
{
    __int64 result;

    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 52))) & (0x3FFFFFFFULL));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 44))) - ((unsigned int)(a3)));
    if (a2 >= result) {
        a2 = result - 1;
    }
    return *(unsigned __int64 *)(a1 + 8) + a2 * 8;
}
```

## 5. (Beta) C Style

```c
int64_t MiComputeContiguousSubsectionPte(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x34))) & (0x3FFFFFFFULL));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x2C))) - ((uint32_t)(a3)));
    if (Arg2 >= result) {
        Arg2 = result - 1;
    }
    return *(uint64_t *)(arg1 + 0x8) + Arg2 * 8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x2C` | `32` | `R` |
| `Arg1` | `+ 0x34` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00444E10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00444E10[BB_00444E10]
  bb_00444E26[BB_00444E26]
  bb_00444E29[BB_00444E29]
  bb_00444E32[BB_00444E32]
  bb_00444E10 -->|branch| bb_00444E29
  bb_00444E10 -->|fallthrough| bb_00444E26
  bb_00444E26 -->|flow| bb_00444E29
```
