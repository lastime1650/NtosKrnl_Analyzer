# ExInitLicenseCallback

- RVA: `0x007C7B14`–`0x007C7B52` (길이 `62` bytes)
- VA: `0x00000001407C7B14`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `62/62` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007C7B1A` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x007C7B3A` → [ExCreateCallback](../A7/ExCreateCallback_function_00A7B9D0.md) (function, `0x00A7B9D0`)

### Direct callers
- [Phase1InitializationDiscard](../../init/C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1D351`

### Static image references
- `0x007C7B22` → RVA `0x00B4C430` (`PAGE`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007C7B1A` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007C7B14  40 53                           push rbx
007C7B16  48 83 EC 20                     sub rsp, 0x20
007C7B1A  E8 D1 66 B3 FF                  call 0x1402fe1f0
007C7B1F  41 B1 01                        mov r9b, 1
007C7B22  48 8D 15 07 49 38 00            lea rdx, [rip + 0x384907]
007C7B29  45 8A C1                        mov r8b, r9b
007C7B2C  48 8B 98 68 03 00 00            mov rbx, qword ptr [rax + 0x368]
007C7B33  48 8D 8B 00 B7 00 00            lea rcx, [rbx + 0xb700]
007C7B3A  E8 91 3E 2B 00                  call 0x140a7b9d0
007C7B3F  85 C0                           test eax, eax
007C7B41  79 08                           jns 0x1407c7b4b
007C7B43  48 83 A3 00 B7 00 00 00         and qword ptr [rbx + 0xb700], 0
007C7B4B  48 83 C4 20                     add rsp, 0x20
007C7B4F  5B                              pop rbx
007C7B50  C3                              ret
007C7B51  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExInitLicenseCallback(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    result = ExCreateCallback(*(unsigned __int64 *)(result + 872) + 46848, v_rip + 3688711, 1, 1);
    if (sign_flag) {
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
void ExInitLicenseCallback(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    result = ExCreateCallback(*(uint64_t *)(result + 0x368) + 46848, v_rip + 3688711, 1, 1);
    if (sign_flag) {
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007C7B14&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007C7B14[BB_007C7B14]
  bb_007C7B43[BB_007C7B43]
  bb_007C7B4B[BB_007C7B4B]
  bb_007C7B51[BB_007C7B51]
  bb_007C7B14 -->|branch| bb_007C7B4B
  bb_007C7B14 -->|fallthrough| bb_007C7B43
  bb_007C7B43 -->|flow| bb_007C7B4B
```
