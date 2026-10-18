# PidNodeCompare

- RVA: `0x007BCF10`–`0x007BCF2A` (길이 `26` bytes)
- VA: `0x00000001407BCF10`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [EtwpGetPrivateSessionTraceHandle](EtwpGetPrivateSessionTraceHandle_function_007BC5A8.md) at `0x007BC6EE`
- [EtwpRegisterPrivateSession](EtwpRegisterPrivateSession_function_007BC92C.md) at `0x007BCA14`
- [EtwpDemuxPrivateTraceHandle](../AC/EtwpDemuxPrivateTraceHandle_function_00ACDB1C.md) at `0x00ACDBCE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007BCF10  44 8B 01                        mov r8d, dword ptr [rcx]
007BCF13  8B 4A 18                        mov ecx, dword ptr [rdx + 0x18]
007BCF16  44 3B C1                        cmp r8d, ecx
007BCF19  73 05                           jae 0x1407bcf20
007BCF1B  83 C8 FF                        or eax, 0xffffffff
007BCF1E  C3                              ret
007BCF1F  CC                              int3
007BCF20  33 C0                           xor eax, eax
007BCF22  44 3B C1                        cmp r8d, ecx
007BCF25  0F 97 C0                        seta al
007BCF28  C3                              ret
007BCF29  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PidNodeCompare(__int64 a1, __int64 a2)
{
    __int64 result;

    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 24))))) goto loc_007BCF20;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    return result;
loc_007BCF20:
    result = 0;
    result = (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 24))))) ? 1 : 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PidNodeCompare(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x18))))) goto loc_007BCF20;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    return result;
loc_007BCF20:
    result = 0;
    result = (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x18))))) ? 1 : 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x18` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007BCF10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007BCF10[BB_007BCF10]
  bb_007BCF1B[BB_007BCF1B]
  bb_007BCF1F[BB_007BCF1F]
  bb_007BCF20[BB_007BCF20]
  bb_007BCF29[BB_007BCF29]
  bb_007BCF10 -->|branch| bb_007BCF20
  bb_007BCF10 -->|fallthrough| bb_007BCF1B
  bb_007BCF1F -->|flow| bb_007BCF20
```
