# KseHookMmMapIoSpace

- RVA: `0x005CD500`–`0x005CD52D` (길이 `45` bytes)
- VA: `0x00000001405CD500`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `13`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005CD522` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005CD51B` → RVA `0x00E01828` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CD500  48 83 EC 28                     sub rsp, 0x28
005CD504  0F 20 D8                        mov rax, cr3
005CD507  48 33 C1                        xor rax, rcx
005CD50A  48 A9 00 F0 FF FF               test rax, -0x1000
005CD510  75 09                           jne 0x1405cd51b
005CD512  F6 C1 03                        test cl, 3
005CD515  74 04                           je 0x1405cd51b
005CD517  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
005CD51B  48 8B 05 06 43 83 00            mov rax, qword ptr [rip + 0x834306]
005CD522  E8 A9 D5 0E 00                  call 0x1406baad0
005CD527  48 83 C4 28                     add rsp, 0x28
005CD52B  C3                              ret
005CD52C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KseHookMmMapIoSpace(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (v_cr3) ^ (a1);
    if (((result) & (0xFFFFFFFFFFFFF000ULL)) != 0) goto loc_005CD51B;
    if ((((unsigned __int8)(a1)) & (3)) != 0) {
        a1 = (a1) & (-4);
    }
    result = guard_dispatch_icall(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KseHookMmMapIoSpace(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (v_cr3) ^ (Arg1);
    if (((result) & (0xFFFFFFFFFFFFF000ULL)) != 0) goto loc_005CD51B;
    if ((((uint8_t)(Arg1)) & (3)) != 0) {
        Arg1 = (Arg1) & (-4);
    }
    result = guard_dispatch_icall(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CD500&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CD500[BB_005CD500]
  bb_005CD512[BB_005CD512]
  bb_005CD517[BB_005CD517]
  bb_005CD51B[BB_005CD51B]
  bb_005CD52C[BB_005CD52C]
  bb_005CD500 -->|branch| bb_005CD51B
  bb_005CD500 -->|fallthrough| bb_005CD512
  bb_005CD512 -->|branch| bb_005CD51B
  bb_005CD512 -->|fallthrough| bb_005CD517
  bb_005CD517 -->|flow| bb_005CD51B
```
