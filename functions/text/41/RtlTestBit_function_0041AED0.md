# RtlTestBit

- RVA: `0x0041AED0`–`0x0041AEEC` (길이 `28` bytes)
- VA: `0x000000014041AED0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `28/28` bytes 표시
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
0041AED0  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0041AED4  44 8B C2                        mov r8d, edx
0041AED7  80 E2 07                        and dl, 7
0041AEDA  49 C1 E8 03                     shr r8, 3
0041AEDE  0F B6 CA                        movzx ecx, dl
0041AEE1  41 0F B6 04 00                  movzx eax, byte ptr [r8 + rax]
0041AEE6  D2 F8                           sar al, cl
0041AEE8  24 01                           and al, 1
0041AEEA  C3                              ret
0041AEEB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlTestBit(__int64 a1, int a2)
{
    __int64 result;

    a2 = (unsigned __int8)((a2) & (7));
    a3 = ((unsigned int)(a2)) >> (3);
    result = (unsigned __int8)((*(unsigned __int8 *)(a3 + *(unsigned __int64 *)(a1 + 8) * 1)) >> ((unsigned __int8)((unsigned __int8)(a2))));
    result = (unsigned __int8)((result) & (1));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlTestBit(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    Arg2 = (uint8_t)((Arg2) & (7));
    a3 = ((uint32_t)(Arg2)) >> (3);
    result = (uint8_t)((*(uint8_t *)(a3 + *(uint64_t *)(arg1 + 0x8) * 1)) >> ((uint8_t)((uint8_t)(Arg2))));
    result = (uint8_t)((result) & (1));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0041AED0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0041AED0[BB_0041AED0]
  bb_0041AEEB[BB_0041AEEB]
```
