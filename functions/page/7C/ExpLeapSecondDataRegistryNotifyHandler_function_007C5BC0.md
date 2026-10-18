# ExpLeapSecondDataRegistryNotifyHandler

- RVA: `0x007C5BC0`–`0x007C5BD8` (길이 `24` bytes)
- VA: `0x00000001407C5BC0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007C5BCD` → [ExpReadLeapSecondData](ExpReadLeapSecondData_function_007C5EAC.md) (function, `0x007C5EAC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x007C5BC4` → RVA `0x00EFEE38` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007C5BC0  48 83 EC 28                     sub rsp, 0x28
007C5BC4  48 8B 0D 6D 92 73 00            mov rcx, qword ptr [rip + 0x73926d]
007C5BCB  B2 01                           mov dl, 1
007C5BCD  E8 DA 02 00 00                  call 0x1407c5eac
007C5BD2  48 83 C4 28                     add rsp, 0x28
007C5BD6  C3                              ret
007C5BD7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpLeapSecondDataRegistryNotifyHandler(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExpReadLeapSecondData(*(unsigned __int64 *)(v_rip + 7574125), 1, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void ExpLeapSecondDataRegistryNotifyHandler(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExpReadLeapSecondData(*(uint64_t *)(v_rip + 0x73926D), 1, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007C5BC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007C5BC0[BB_007C5BC0]
  bb_007C5BD7[BB_007C5BD7]
```
