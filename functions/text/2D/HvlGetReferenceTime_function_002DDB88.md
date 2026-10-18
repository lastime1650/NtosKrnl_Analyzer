# HvlGetReferenceTime

- RVA: `0x002DDB88`–`0x002DDBB5` (길이 `45` bytes)
- VA: `0x00000001402DDB88`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000704D0`
- 디코드: `13`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x002DDB9A` → [HvlGetReferenceTimeUsingTscPage](HvlGetReferenceTimeUsingTscPage_function_002DDBC0.md) (function, `0x002DDBC0`)

### Direct callers
- [sub_002D7E2F](Unknown_function_002D7E2F.md) at `0x002D7E38`
- [PpmUpdatePerformanceFeedback](PpmUpdatePerformanceFeedback_function_002DE580.md) at `0x002DEE5D`
- [PpmHvSnapPerformanceAccumulation](../44/PpmHvSnapPerformanceAccumulation_function_0044FA34.md) at `0x0044FAE5`

### Static image references
- `0x002DDB8C` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002DDB88  48 83 EC 28                     sub rsp, 0x28
002DDB8C  F7 05 22 8F CE 00 00 01 00 00   test dword ptr [rip + 0xce8f22], 0x100
002DDB96  74 0D                           je 0x1402ddba5
002DDB98  33 C9                           xor ecx, ecx
002DDB9A  E8 21 00 00 00                  call 0x1402ddbc0
002DDB9F  48 83 C4 28                     add rsp, 0x28
002DDBA3  C3                              ret
002DDBA4  CC                              int3
002DDBA5  B9 20 00 00 40                  mov ecx, 0x40000020
002DDBAA  0F 32                           rdmsr
002DDBAC  48 C1 E2 20                     shl rdx, 0x20
002DDBB0  48 0B C2                        or rax, rdx
002DDBB3  EB EA                           jmp 0x1402ddb9f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlGetReferenceTime(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((*(unsigned int *)(v_rip + 13537058)) & (256)) == 0) goto loc_002DDBA5;
    a1 = 0;
    result = HvlGetReferenceTimeUsingTscPage(a1, a2, a3, a4);
loc_002DDB9F:
    v_rsp = (v_rsp) + (40);
    return result;
loc_002DDBA5:
    a2 = (a2) << (32);
    result = (result) | (a2);
    goto loc_002DDB9F;
}
```

## 5. (Beta) C Style

```c
int64_t HvlGetReferenceTime(int32_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((*(uint32_t *)(v_rip + 0xCE8F22)) & (256)) == 0) goto loc_002DDBA5;
    Arg1 = 0;
    result = HvlGetReferenceTimeUsingTscPage(Arg1, Arg2, a3, a4);
loc_002DDB9F:
    local_rsp = (local_rsp) + (40);
    return result;
loc_002DDBA5:
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    goto loc_002DDB9F;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002DDB88&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002DDB88[BB_002DDB88]
  bb_002DDB98[BB_002DDB98]
  bb_002DDB9F[BB_002DDB9F]
  bb_002DDBA4[BB_002DDBA4]
  bb_002DDBA5[BB_002DDBA5]
  bb_002DDB88 -->|branch| bb_002DDBA5
  bb_002DDB88 -->|fallthrough| bb_002DDB98
  bb_002DDB98 -->|flow| bb_002DDB9F
  bb_002DDBA4 -->|flow| bb_002DDBA5
  bb_002DDBA5 -->|branch| bb_002DDB9F
```
