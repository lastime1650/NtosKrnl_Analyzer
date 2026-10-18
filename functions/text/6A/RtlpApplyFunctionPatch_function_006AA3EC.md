# RtlpApplyFunctionPatch

- RVA: `0x006AA3EC`–`0x006AA400` (길이 `20` bytes)
- VA: `0x00000001406AA3EC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `7`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlApplyHotPatch](../../pagelk/B7/RtlApplyHotPatch_function_00B7528C.md) at `0x00B756DA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006AA3EC  8B 44 24 28                     mov eax, dword ptr [rsp + 0x28]
006AA3F0  2B C2                           sub eax, edx
006AA3F2  C6 41 FB E9                     mov byte ptr [rcx - 5], 0xe9
006AA3F6  89 41 FC                        mov dword ptr [rcx - 4], eax
006AA3F9  66 C7 01 EB F9                  mov word ptr [rcx], 0xf9eb
006AA3FE  C3                              ret
006AA3FF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpApplyFunctionPatch(__int64 a1, int a2, __int64 a3, __int64 a4, unsigned int a5)
{
    __int64 result;

    result = (unsigned int)(((unsigned int)(a5)) - (a2));
    *(unsigned __int8 *)(a1 - 5) = 233;
    *(unsigned int *)(a1 - 4) = (unsigned int)(result);
    *(unsigned __int16 *)(a1) = 0xF9EBULL;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpApplyFunctionPatch(void *Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = (uint32_t)(((uint32_t)(Arg5)) - (Arg2));
    *(uint8_t *)(arg1 - 0x5) = 233;
    *(uint32_t *)(arg1 - 0x4) = (uint32_t)(result);
    *(uint16_t *)(arg1) = 0xF9EBULL;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x5` | `8` | `W` |
| `Arg1` | `- 0x4` | `32` | `W` |
| `Arg1` | `+ 0x0` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AA3EC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AA3EC[BB_006AA3EC]
  bb_006AA3FF[BB_006AA3FF]
```
