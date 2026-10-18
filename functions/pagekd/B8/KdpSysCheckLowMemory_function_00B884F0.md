# KdpSysCheckLowMemory

- RVA: `0x00B884F0`–`0x00B8850B` (길이 `27` bytes)
- VA: `0x0000000140B884F0`
- 실행 섹션: `PAGEKD`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B884FE` → [KdpSearchPhysicalPageRange](KdpSearchPhysicalPageRange_function_00B882F4.md) (function, `0x00B882F4`)

### Direct callers
- [KdSystemDebugControl](../../page/74/KdSystemDebugControl_function_00744700.md) at `0x00744C3B`
- [KdpCheckLowMemory](KdpCheckLowMemory_function_00B870B0.md) at `0x00B870D3`

### Static image references
- `0x00B884F4` → RVA `0x00F51B88` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B884F0  48 83 EC 28                     sub rsp, 0x28
00B884F4  8B 05 8E 96 3C 00               mov eax, dword ptr [rip + 0x3c968e]
00B884FA  85 C0                           test eax, eax
00B884FC  74 05                           je 0x140b88503
00B884FE  E8 F1 FD FF FF                  call 0x140b882f4
00B88503  33 C0                           xor eax, eax
00B88505  48 83 C4 28                     add rsp, 0x28
00B88509  C3                              ret
00B8850A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KdpSysCheckLowMemory(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (unsigned int)(*(unsigned int *)(v_rip + 3970702));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3970702))) != 0) {
        result = KdpSearchPhysicalPageRange(a1, a2, a3, a4);
    }
    result = 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void KdpSysCheckLowMemory(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x3C968E));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3C968E))) != 0) {
        result = KdpSearchPhysicalPageRange(a1, a2, a3, a4);
    }
    result = 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagekd&rva=0x00B884F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B884F0[BB_00B884F0]
  bb_00B884FE[BB_00B884FE]
  bb_00B88503[BB_00B88503]
  bb_00B8850A[BB_00B8850A]
  bb_00B884F0 -->|branch| bb_00B88503
  bb_00B884F0 -->|fallthrough| bb_00B884FE
  bb_00B884FE -->|flow| bb_00B88503
```
