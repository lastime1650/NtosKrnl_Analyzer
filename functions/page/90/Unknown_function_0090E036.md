# sub_0090E036

- RVA: `0x0090E036`–`0x0090E04F` (길이 `25` bytes)
- VA: `0x000000014090E036`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008962C`
- 디코드: `7`개 명령, `25/25` bytes 표시
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
  - `0x0090E04A` → [RtlCustomCPToUnicodeN + 0x82](RtlCustomCPToUnicodeN_function_0090DEE0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0090E036  8B C3                           mov eax, ebx
0090E038  41 89 18                        mov dword ptr [r8], ebx
0090E03B  3D 23 00 00 C0                  cmp eax, 0xc0000023
0090E040  B9 05 00 00 80                  mov ecx, 0x80000005
0090E045  0F 44 D9                        cmove ebx, ecx
0090E048  8B C3                           mov eax, ebx
0090E04A  E9 13 FF FF FF                  jmp 0x14090df62
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0090E036(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 v_rbx;

    *(unsigned int *)(a3) = (unsigned int)(v_rbx);
    if (((unsigned int)((unsigned int)((unsigned int)(v_rbx)))) == 0xC0000023ULL) { v_rbx = (unsigned int)((unsigned int)(0x80000005ULL)); }
}
```

## 5. (Beta) C Style

```c
int64_t sub_0090E036(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t local_rbx;

    *(uint32_t *)(arg3) = (uint32_t)(local_rbx);
    if (((uint32_t)((uint32_t)((uint32_t)(local_rbx)))) == 0xC0000023ULL) { local_rbx = (uint32_t)((uint32_t)(0x80000005ULL)); }
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0090E036&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0090E036[BB_0090E036]
```
