# EmonResumeProfilingEnhanced

- RVA: `0x0055F950`–`0x0055F983` (길이 `51` bytes)
- VA: `0x000000014055F950`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `15`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0055F962` → [EmonResumeProfilingInternalEnhanced](EmonResumeProfilingInternalEnhanced_function_0055F98C.md) (function, `0x0055F98C`)
- `0x0055F977` → [EmonResumeProfilingInternalEnhanced](EmonResumeProfilingInternalEnhanced_function_0055F98C.md) (function, `0x0055F98C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0055F967` → RVA `0x00F8FDE0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0055F950  40 53                           push rbx
0055F952  48 83 EC 20                     sub rsp, 0x20
0055F956  65 8B 1C 25 A4 01 00 00         mov ebx, dword ptr gs:[0x1a4]
0055F95E  33 C9                           xor ecx, ecx
0055F960  8B D3                           mov edx, ebx
0055F962  E8 25 00 00 00                  call 0x14055f98c
0055F967  83 3D 72 04 A3 00 02            cmp dword ptr [rip + 0xa30472], 2
0055F96E  72 0C                           jb 0x14055f97c
0055F970  8B D3                           mov edx, ebx
0055F972  B9 01 00 00 00                  mov ecx, 1
0055F977  E8 10 00 00 00                  call 0x14055f98c
0055F97C  48 83 C4 20                     add rsp, 0x20
0055F980  5B                              pop rbx
0055F981  C3                              ret
0055F982  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EmonResumeProfilingEnhanced(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = 0;
    result = EmonResumeProfilingInternalEnhanced(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))), a3, a4);
    if ((*(unsigned int *)(v_rip + 10683506)) >= 2) {
        a2 = (unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))));
        a1 = 1;
        result = EmonResumeProfilingInternalEnhanced(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EmonResumeProfilingEnhanced(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = 0;
    result = EmonResumeProfilingInternalEnhanced(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))), a3, a4);
    if ((*(uint32_t *)(v_rip + 0xA30472)) >= 2) {
        a2 = (uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))));
        Arg1 = 1;
        result = EmonResumeProfilingInternalEnhanced(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0055F950&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0055F950[BB_0055F950]
  bb_0055F970[BB_0055F970]
  bb_0055F97C[BB_0055F97C]
  bb_0055F982[BB_0055F982]
  bb_0055F950 -->|branch| bb_0055F97C
  bb_0055F950 -->|fallthrough| bb_0055F970
  bb_0055F970 -->|flow| bb_0055F97C
```
