# RtlSubtreeSuccessor

- RVA: `0x005EBDB0`–`0x005EBDCF` (길이 `31` bytes)
- VA: `0x00000001405EBDB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `13`개 명령, `31/31` bytes 표시
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
005EBDB0  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
005EBDB4  48 85 C0                        test rax, rax
005EBDB7  74 14                           je 0x1405ebdcd
005EBDB9  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
005EBDBD  EB 07                           jmp 0x1405ebdc6
005EBDBF  48 8B C1                        mov rax, rcx
005EBDC2  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
005EBDC6  48 85 C9                        test rcx, rcx
005EBDC9  75 F4                           jne 0x1405ebdbf
005EBDCB  C3                              ret
005EBDCC  CC                              int3
005EBDCD  C3                              ret
005EBDCE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlSubtreeSuccessor(__int64 a1)
{
    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_005EBDCD;
    goto loc_005EBDC6;
loc_005EBDBF:
loc_005EBDC6:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 8) != 0) goto loc_005EBDBF;
    return *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8);
loc_005EBDCD:
    return *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8);
}
```

## 5. (Beta) C Style

```c
int64_t RtlSubtreeSuccessor(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if (*(uint64_t *)(arg1 + 0x10) == 0) goto loc_005EBDCD;
    goto loc_005EBDC6;
loc_005EBDBF:
loc_005EBDC6:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x8) != 0) goto loc_005EBDBF;
    return *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8);
loc_005EBDCD:
    return *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005EBDB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005EBDB0[BB_005EBDB0]
  bb_005EBDB9[BB_005EBDB9]
  bb_005EBDBF[BB_005EBDBF]
  bb_005EBDC6[BB_005EBDC6]
  bb_005EBDCB[BB_005EBDCB]
  bb_005EBDCC[BB_005EBDCC]
  bb_005EBDCD[BB_005EBDCD]
  bb_005EBDCE[BB_005EBDCE]
  bb_005EBDB0 -->|branch| bb_005EBDCD
  bb_005EBDB0 -->|fallthrough| bb_005EBDB9
  bb_005EBDB9 -->|branch| bb_005EBDC6
  bb_005EBDBF -->|flow| bb_005EBDC6
  bb_005EBDC6 -->|branch| bb_005EBDBF
  bb_005EBDC6 -->|fallthrough| bb_005EBDCB
  bb_005EBDCC -->|flow| bb_005EBDCD
```
