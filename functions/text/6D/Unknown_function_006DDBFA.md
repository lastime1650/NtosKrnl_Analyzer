# sub_006DDBFA

- RVA: `0x006DDBFA`–`0x006DDC11` (길이 `23` bytes)
- VA: `0x00000001406DDBFA`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006FE7C`
- 디코드: `6`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006DDC04` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006DDC0C` → [sub_002D6584 + 0x314](../2D/Unknown_function_002D6584.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006DDBFA  41 8B C4                        mov eax, r12d
006DDBFD  8B D0                           mov edx, eax
006DDBFF  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
006DDC04  E8 E7 DA B7 FF                  call 0x14025b6f0
006DDC09  41 8B FD                        mov edi, r13d
006DDC0C  E9 87 8C BF FF                  jmp 0x1402d6898
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006DDBFA(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14)
{
    __int64 result;

    result = KeAddProcessorAffinityEx(a14, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))), a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_006DDBFA(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, int64_t Arg14)
{
    int64_t result;

    result = KeAddProcessorAffinityEx(Arg14, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))), Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006DDBFA&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006DDBFA[BB_006DDBFA]
```
