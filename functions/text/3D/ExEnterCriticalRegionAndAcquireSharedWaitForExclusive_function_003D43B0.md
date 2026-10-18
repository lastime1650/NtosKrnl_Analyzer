# ExEnterCriticalRegionAndAcquireSharedWaitForExclusive

- RVA: `0x003D43B0`–`0x003D43E2` (길이 `50` bytes)
- VA: `0x00000001403D43B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003D43C7` → [ExAcquireSharedWaitForExclusive](ExAcquireSharedWaitForExclusive_function_003D43F0.md) (function, `0x003D43F0`)

### Direct callers
- [DifExEnterCriticalRegionAndAcquireSharedWaitForExclusiveWrapper](../61/DifExEnterCriticalRegionAndAcquireSharedWaitForExclusiveWrapper_function_0061FFD0.md) at `0x0062009D`
- [VerifierExEnterCriticalRegionAndAcquireSharedWaitForExclusive](../../pagevrfy/B9/VerifierExEnterCriticalRegionAndAcquireSharedWaitForExclusive_function_00B9E510.md) at `0x00B9E520`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003D43B0  48 83 EC 28                     sub rsp, 0x28
003D43B4  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003D43BD  B2 01                           mov dl, 1
003D43BF  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
003D43C6  90                              nop
003D43C7  E8 24 00 00 00                  call 0x1403d43f0
003D43CC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003D43D5  48 8B 80 C8 01 00 00            mov rax, qword ptr [rax + 0x1c8]
003D43DC  48 83 C4 28                     add rsp, 0x28
003D43E0  C3                              ret
003D43E1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExEnterCriticalRegionAndAcquireSharedWaitForExclusive(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExAcquireSharedWaitForExclusive(a1, 1, a3, a4);
    v_rsp = (v_rsp) + (40);
    return *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 456);
}
```

## 5. (Beta) C Style

```c
void ExEnterCriticalRegionAndAcquireSharedWaitForExclusive(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExAcquireSharedWaitForExclusive(a1, 1, a3, a4);
    local_rsp = (local_rsp) + (40);
    return *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1C8);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003D43B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003D43B0[BB_003D43B0]
  bb_003D43E1[BB_003D43E1]
```
