# PopNewWakeSource

- RVA: `0x007026A4`–`0x007026CE` (길이 `42` bytes)
- VA: `0x00000001407026A4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `14`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007026BA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [PopHandleWakeSources](../../pagelk/B6/PopHandleWakeSources_function_00B6C264.md) at `0x00B6C37A`
- [PopProcessWakeSourceWork](../../pagelk/B7/PopProcessWakeSourceWork_function_00B7C488.md) at `0x00B7C52B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007026BA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007026A4  40 53                           push rbx
007026A6  48 83 EC 20                     sub rsp, 0x20
007026AA  BA 70 00 00 00                  mov edx, 0x70
007026AF  8B D9                           mov ebx, ecx
007026B1  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
007026B7  8D 4A D0                        lea ecx, [rdx - 0x30]
007026BA  E8 31 FA 47 00                  call 0x140b820f0
007026BF  48 85 C0                        test rax, rax
007026C2  74 03                           je 0x1407026c7
007026C4  89 58 10                        mov dword ptr [rax + 0x10], ebx
007026C7  48 83 C4 20                     add rsp, 0x20
007026CB  5B                              pop rbx
007026CC  C3                              ret
007026CD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopNewWakeSource(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ExAllocatePool2(112 - 48, 112, (unsigned int)(0x206D654DULL), a4);
    if (result != 0) {
        *(unsigned int *)(result + 16) = (unsigned int)((unsigned int)(a1));
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopNewWakeSource(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ExAllocatePool2(112 - 48, 112, (uint32_t)(0x206D654DULL), a4);
    if (result != 0) {
        *(uint32_t *)(result + 0x10) = (uint32_t)((uint32_t)(Arg1));
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007026A4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007026A4[BB_007026A4]
  bb_007026C4[BB_007026C4]
  bb_007026C7[BB_007026C7]
  bb_007026CD[BB_007026CD]
  bb_007026A4 -->|branch| bb_007026C7
  bb_007026A4 -->|fallthrough| bb_007026C4
  bb_007026C4 -->|flow| bb_007026C7
```
