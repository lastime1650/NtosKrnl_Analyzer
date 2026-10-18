# PopPdcEngagePhases

- RVA: `0x007697B4`–`0x007697D7` (길이 `35` bytes)
- VA: `0x00000001407697B4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007697CC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [PopPowerAggregatorEngageAggressiveStandbyActions](PopPowerAggregatorEngageAggressiveStandbyActions_function_0076460C.md) at `0x00764760`
- [PopPowerAggregatorEnterScreenOff](../98/PopPowerAggregatorEnterScreenOff_function_00989F38.md) at `0x0098A0D8`

### Static image references
- `0x007697B8` → RVA `0x00E677D8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007697CC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007697B4  48 83 EC 28                     sub rsp, 0x28
007697B8  48 8B 15 19 E0 6F 00            mov rdx, qword ptr [rip + 0x6fe019]
007697BF  B8 02 00 00 C0                  mov eax, 0xc0000002
007697C4  48 85 D2                        test rdx, rdx
007697C7  74 08                           je 0x1407697d1
007697C9  48 8B C2                        mov rax, rdx
007697CC  E8 FF 12 F5 FF                  call 0x1406baad0
007697D1  48 83 C4 28                     add rsp, 0x28
007697D5  C3                              ret
007697D6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPdcEngagePhases(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (unsigned int)(0xC0000002ULL);
    if (*(unsigned __int64 *)(v_rip + 7331865) != 0) {
        result = *(unsigned __int64 *)(v_rip + 7331865);
        result = guard_dispatch_icall(a1, *(unsigned __int64 *)(v_rip + 7331865), a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PopPdcEngagePhases(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (uint32_t)(0xC0000002ULL);
    if (*(uint64_t *)(v_rip + 0x6FE019) != 0) {
        result = *(uint64_t *)(v_rip + 0x6FE019);
        result = guard_dispatch_icall(a1, *(uint64_t *)(v_rip + 0x6FE019), a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007697B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007697B4[BB_007697B4]
  bb_007697C9[BB_007697C9]
  bb_007697D1[BB_007697D1]
  bb_007697D6[BB_007697D6]
  bb_007697B4 -->|branch| bb_007697D1
  bb_007697B4 -->|fallthrough| bb_007697C9
  bb_007697C9 -->|flow| bb_007697D1
```
