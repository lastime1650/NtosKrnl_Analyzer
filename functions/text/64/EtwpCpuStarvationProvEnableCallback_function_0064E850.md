# EtwpCpuStarvationProvEnableCallback

- RVA: `0x0064E850`–`0x0064E864` (길이 `20` bytes)
- VA: `0x000000014064E850`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0064E859` → [KeEtwInitializeCpuStarvationProvider](../5B/KeEtwInitializeCpuStarvationProvider_function_005B5704.md) (function, `0x005B5704`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0064E850  48 83 EC 28                     sub rsp, 0x28
0064E854  83 FA 01                        cmp edx, 1
0064E857  75 05                           jne 0x14064e85e
0064E859  E8 A6 6E F6 FF                  call 0x1405b5704
0064E85E  48 83 C4 28                     add rsp, 0x28
0064E862  C3                              ret
0064E863  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpCpuStarvationProvEnableCallback(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a2 == 1) {
        result = KeEtwInitializeCpuStarvationProvider(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpCpuStarvationProvEnableCallback(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg2 == 1) {
        result = KeEtwInitializeCpuStarvationProvider(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0064E850&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0064E850[BB_0064E850]
  bb_0064E859[BB_0064E859]
  bb_0064E85E[BB_0064E85E]
  bb_0064E863[BB_0064E863]
  bb_0064E850 -->|branch| bb_0064E85E
  bb_0064E850 -->|fallthrough| bb_0064E859
  bb_0064E859 -->|flow| bb_0064E85E
```
