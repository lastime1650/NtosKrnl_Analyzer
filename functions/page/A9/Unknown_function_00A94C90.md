# sub_00A94C90

- RVA: `0x00A94C90`–`0x00A94CA9` (길이 `25` bytes)
- VA: `0x0000000140A94C90`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `25/25` bytes 표시
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
00A94C90  4C 8B 02                        mov r8, qword ptr [rdx]
00A94C93  4C 2B 41 20                     sub r8, qword ptr [rcx + 0x20]
00A94C97  75 0B                           jne 0x140a94ca4
00A94C99  8B 41 18                        mov eax, dword ptr [rcx + 0x18]
00A94C9C  8B 4A 08                        mov ecx, dword ptr [rdx + 8]
00A94C9F  2B C8                           sub ecx, eax
00A94CA1  4C 63 C1                        movsxd r8, ecx
00A94CA4  49 8B C0                        mov rax, r8
00A94CA7  C3                              ret
00A94CA8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00A94C90(__int64 a1, __int64 a2)
{
    __int64 result;

    a3 = (*(unsigned __int64 *)(a2)) - (*(unsigned __int64 *)(a1 + 32));
    if (!(condition_is_not_equal)) {
        result = *(unsigned int *)(a1 + 24);
        a1 = *(unsigned int *)(a2 + 8);
        a1 = (unsigned int)((a1) - ((unsigned int)(result)));
        a3 = (int)((unsigned int)(a1));
    }
    return a3;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00A94C90(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    a3 = (*(uint64_t *)(arg2)) - (*(uint64_t *)(arg1 + 0x20));
    if (!(condition_is_not_equal)) {
        result = *(uint32_t *)(arg1 + 0x18);
        Arg1 = *(uint32_t *)(arg2 + 0x8);
        Arg1 = (uint32_t)((Arg1) - ((uint32_t)(result)));
        a3 = (int32_t)((uint32_t)(Arg1));
    }
    return a3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A94C90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A94C90[BB_00A94C90]
  bb_00A94C99[BB_00A94C99]
  bb_00A94CA4[BB_00A94CA4]
  bb_00A94CA8[BB_00A94CA8]
  bb_00A94C90 -->|branch| bb_00A94CA4
  bb_00A94C90 -->|fallthrough| bb_00A94C99
  bb_00A94C99 -->|flow| bb_00A94CA4
```
