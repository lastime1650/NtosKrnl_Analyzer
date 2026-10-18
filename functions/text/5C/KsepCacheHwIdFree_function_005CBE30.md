# KsepCacheHwIdFree

- RVA: `0x005CBE30`–`0x005CBE55` (길이 `37` bytes)
- VA: `0x00000001405CBE30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000805BC`
- 디코드: `13`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005CBE41` → [KsepStringFree](../../page/95/KsepStringFree_function_0095A1B8.md) (function, `0x0095A1B8`)
- `0x005CBE49` → [KsepPoolFreePaged](../4B/KsepPoolFreePaged_function_004B0E10.md) (function, `0x004B0E10`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x005CBE41` → [KsepStringFree](../../page/95/KsepStringFree_function_0095A1B8.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CBE30  48 85 C9                        test rcx, rcx
005CBE33  74 1E                           je 0x1405cbe53
005CBE35  53                              push rbx
005CBE36  48 83 EC 20                     sub rsp, 0x20
005CBE3A  48 8B D9                        mov rbx, rcx
005CBE3D  48 83 C1 28                     add rcx, 0x28
005CBE41  E8 72 E3 38 00                  call 0x14095a1b8
005CBE46  48 8B CB                        mov rcx, rbx
005CBE49  E8 C2 4F EE FF                  call 0x1404b0e10
005CBE4E  48 83 C4 20                     add rsp, 0x20
005CBE52  5B                              pop rbx
005CBE53  C3                              ret
005CBE54  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KsepCacheHwIdFree(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    if (a1 != 0) {
        v_rsp = (v_rsp) - (32);
        v_rbx = a1;
        a1 = (a1) + (40);
        result = KsepStringFree(a1, a2, a3, a4);
        a1 = v_rbx;
        result = KsepPoolFreePaged(a1, a2, a3, a4);
        v_rsp = (v_rsp) + (32);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KsepCacheHwIdFree(int64_t Arg1)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    if (Arg1 != 0) {
        local_rsp = (local_rsp) - (32);
        local_rbx = Arg1;
        Arg1 = (Arg1) + (40);
        result = KsepStringFree(Arg1, a2, a3, a4);
        Arg1 = local_rbx;
        result = KsepPoolFreePaged(Arg1, a2, a3, a4);
        local_rsp = (local_rsp) + (32);
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CBE30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CBE30[BB_005CBE30]
  bb_005CBE35[BB_005CBE35]
  bb_005CBE53[BB_005CBE53]
  bb_005CBE54[BB_005CBE54]
  bb_005CBE30 -->|branch| bb_005CBE53
  bb_005CBE30 -->|fallthrough| bb_005CBE35
  bb_005CBE35 -->|flow| bb_005CBE53
```
