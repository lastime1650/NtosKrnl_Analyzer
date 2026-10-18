# ReadAMDMsr

- RVA: `0x006B9ED0`–`0x006B9EE7` (길이 `23` bytes)
- VA: `0x00000001406B9ED0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C23A8`
- 디코드: `7`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiDisableCacheErrataSource](../5C/KiDisableCacheErrataSource_function_005C4DC8.md) at `0x005C4DF7`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006B9ED0  48 57                           push rdi
006B9ED2  48 BF 3A 20 5A 9C 00 00 00 00   movabs rdi, 0x9c5a203a
006B9EDC  0F 32                           rdmsr
006B9EDE  48 C1 E2 20                     shl rdx, 0x20
006B9EE2  48 0B C2                        or rax, rdx
006B9EE5  5F                              pop rdi
006B9EE6  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ReadAMDMsr(__int64 a1, __int64 a2)
{
    __int64 result;

    a2 = (a2) << (32);
    result = (result) | (a2);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ReadAMDMsr(int64_t Arg1, int64_t Arg2)
{
    int64_t result;

    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006B9ED0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006B9ED0[BB_006B9ED0]
```
