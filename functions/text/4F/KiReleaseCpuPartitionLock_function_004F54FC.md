# KiReleaseCpuPartitionLock

- RVA: `0x004F54FC`–`0x004F552D` (길이 `49` bytes)
- VA: `0x00000001404F54FC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `15`개 명령, `49/49` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004F5509` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x004F551D` → [KiLowerIrqlProcessIrqlFlags](KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)

### Direct callers
- [KeModifySystemAllowedCpuSets](../30/KeModifySystemAllowedCpuSets_function_00303308.md) at `0x00303356`
- [KiQueryCpuPartitionAffinity](KiQueryCpuPartitionAffinity_function_004F548C.md) at `0x004F54E5`
- [KeQueryCpuPartitionAffinity](../5C/KeQueryCpuPartitionAffinity_function_005C0EF8.md) at `0x005C0F92`

### Static image references
- `0x004F550E` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F54FC  40 53                           push rbx
004F54FE  48 83 EC 20                     sub rsp, 0x20
004F5502  48 83 C1 08                     add rcx, 8
004F5506  0F B6 DA                        movzx ebx, dl
004F5509  E8 62 11 D1 FF                  call 0x140206670
004F550E  83 3D 0B 18 AD 00 00            cmp dword ptr [rip + 0xad180b], 0
004F5515  74 0B                           je 0x1404f5522
004F5517  44 0F 20 C1                     mov rcx, cr8
004F551B  8A D3                           mov dl, bl
004F551D  E8 76 01 00 00                  call 0x1404f5698
004F5522  44 0F 22 C3                     mov cr8, rbx
004F5526  48 83 C4 20                     add rsp, 0x20
004F552A  5B                              pop rbx
004F552B  C3                              ret
004F552C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiReleaseCpuPartitionLock(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = (a1) + (8);
    result = KxReleaseSpinLock(a1, a2, a3, a4);
    if ((*(unsigned int *)(v_rip + 11343883)) != 0) {
        a1 = v_cr8;
        a2 = a2;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiReleaseCpuPartitionLock(int64_t Arg1, uint8_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) + (8);
    result = KxReleaseSpinLock(Arg1, Arg2, a3, a4);
    if ((*(uint32_t *)(v_rip + 0xAD180B)) != 0) {
        Arg1 = v_cr8;
        Arg2 = Arg2;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F54FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F54FC[BB_004F54FC]
  bb_004F5517[BB_004F5517]
  bb_004F5522[BB_004F5522]
  bb_004F552C[BB_004F552C]
  bb_004F54FC -->|branch| bb_004F5522
  bb_004F54FC -->|fallthrough| bb_004F5517
  bb_004F5517 -->|flow| bb_004F5522
```
