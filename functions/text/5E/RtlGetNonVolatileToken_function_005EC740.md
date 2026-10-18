# RtlGetNonVolatileToken

- RVA: `0x005EC740`–`0x005EC759` (길이 `25` bytes)
- VA: `0x00000001405EC740`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005EC740` → RVA `0x00E0C5BC` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005EC740  80 3D 75 FE 81 00 00            cmp byte ptr [rip + 0x81fe75], 0
005EC747  B8 01 00 00 00                  mov eax, 1
005EC74C  8D 48 02                        lea ecx, [rax + 2]
005EC74F  0F 45 C1                        cmovne eax, ecx
005EC752  49 89 00                        mov qword ptr [r8], rax
005EC755  33 C0                           xor eax, eax
005EC757  C3                              ret
005EC758  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlGetNonVolatileToken(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;

    result = 1;
    if ((*(unsigned __int8 *)(v_rip + 8519285)) != 0) { result = (unsigned int)(1 + 2); }
    *(unsigned __int64 *)(a3) = result;
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlGetNonVolatileToken(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    result = 1;
    if ((*(uint8_t *)(v_rip + 0x81FE75)) != 0) { result = (uint32_t)(1 + 2); }
    *(uint64_t *)(arg3) = result;
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005EC740&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005EC740[BB_005EC740]
  bb_005EC758[BB_005EC758]
```
