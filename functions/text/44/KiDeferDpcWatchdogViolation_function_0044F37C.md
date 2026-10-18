# KiDeferDpcWatchdogViolation

- RVA: `0x0044F37C`–`0x0044F3C1` (길이 `69` bytes)
- VA: `0x000000014044F37C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `69/69` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0044F39D` → [KeRelaxTimingConstraints](../5B/KeRelaxTimingConstraints_function_005B59C8.md) (function, `0x005B59C8`)

### Direct callers
- [KeAccumulateTicks](../39/KeAccumulateTicks_function_0039C140.md) at `0x0039C7D9`

### Static image references
- `0x0044F38D` → RVA `0x00F10850` (`.data`; read)
- `0x0044F3A8` → RVA `0x00F10858` (`.data`; write)
- `0x0044F3B4` → RVA `0x00F1085C` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0044F37C  40 53                           push rbx
0044F37E  48 83 EC 20                     sub rsp, 0x20
0044F382  65 48 8B 1C 25 20 00 00 00      mov rbx, qword ptr gs:[0x20]
0044F38B  33 C0                           xor eax, eax
0044F38D  F0 48 0F B1 1D BA 14 AC 00      lock cmpxchg qword ptr [rip + 0xac14ba], rbx
0044F396  75 22                           jne 0x14044f3ba
0044F398  B9 01 00 00 00                  mov ecx, 1
0044F39D  E8 26 66 16 00                  call 0x1405b59c8
0044F3A2  8B 83 5C 86 00 00               mov eax, dword ptr [rbx + 0x865c]
0044F3A8  89 05 AA 14 AC 00               mov dword ptr [rip + 0xac14aa], eax
0044F3AE  8B 83 60 86 00 00               mov eax, dword ptr [rbx + 0x8660]
0044F3B4  89 05 A2 14 AC 00               mov dword ptr [rip + 0xac14a2], eax
0044F3BA  48 83 C4 20                     add rsp, 0x20
0044F3BE  5B                              pop rbx
0044F3BF  C3                              ret
0044F3C0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiDeferDpcWatchdogViolation(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = 0;
    if (!(condition_is_not_equal)) {
        a1 = 1;
        result = KeRelaxTimingConstraints(a1, a2, a3, a4);
        result = *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34396);
        *(unsigned int *)(v_rip + 11277482) = (unsigned int)(result);
        result = *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34400);
        *(unsigned int *)(v_rip + 11277474) = (unsigned int)(result);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
void KiDeferDpcWatchdogViolation(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = 0;
    if (!(condition_is_not_equal)) {
        a1 = 1;
        result = KeRelaxTimingConstraints(a1, a2, a3, a4);
        result = *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x865C);
        *(uint32_t *)(v_rip + 0xAC14AA) = (uint32_t)(result);
        result = *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8660);
        *(uint32_t *)(v_rip + 0xAC14A2) = (uint32_t)(result);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0044F37C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0044F37C[BB_0044F37C]
  bb_0044F398[BB_0044F398]
  bb_0044F3BA[BB_0044F3BA]
  bb_0044F3C0[BB_0044F3C0]
  bb_0044F37C -->|branch| bb_0044F3BA
  bb_0044F37C -->|fallthrough| bb_0044F398
  bb_0044F398 -->|flow| bb_0044F3BA
```
