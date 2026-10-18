# sub_006F601A

- RVA: `0x006F601A`–`0x006F602E` (길이 `20` bytes)
- VA: `0x00000001406F601A`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B0140`
- 디코드: `5`개 명령, `20/20` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006F6029` → [HalpInterruptFindBestRouting + 0x57](../48/HalpInterruptFindBestRouting_function_0048A784.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F601A  41 8B 42 10                     mov eax, dword ptr [r10 + 0x10]
006F601E  41 89 00                        mov dword ptr [r8], eax
006F6021  41 8B 42 14                     mov eax, dword ptr [r10 + 0x14]
006F6025  41 89 40 04                     mov dword ptr [r8 + 4], eax
006F6029  E9 AD 47 D9 FF                  jmp 0x14048a7db
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006F601A(__int64 a1, __int64 a2, __int64 a3)
{
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + 16)));
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + 20)));
}
```

## 5. (Beta) C Style

```c
int64_t sub_006F601A(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + 0x10)));
    *(uint32_t *)(arg3 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + 0x14)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `32` | `W` |
| `Arg3` | `+ 0x4` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F601A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006F601A[BB_006F601A]
```
