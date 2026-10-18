# ZwLoadDriver

- RVA: `0x006AF290`–`0x006AF2AF` (길이 `31` bytes)
- VA: `0x00000001406AF290`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C0B38`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KsepLoadShimProvider](../5C/KsepLoadShimProvider_function_005CBA44.md) at `0x005CBAA1`
- [DifZwLoadDriverWrapper](../64/DifZwLoadDriverWrapper_function_00642A30.md) at `0x00642AFB`
- [PopCadTriggerDriverLoad](../../page/76/PopCadTriggerDriverLoad_function_0076FFC0.md) at `0x0076FFE2`
- [EtwpConstructIptData](../../page/7C/EtwpConstructIptData_function_007C1048.md) at `0x007C105C`
- [EtwpUpdateFileInfoDriverState](../../page/A5/EtwpUpdateFileInfoDriverState_function_00A501BC.md) at `0x00A5026B`
- [NtSetSystemInformation](../../page/AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF5D37`

### Static image references
- `0x006AF29C` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AF2A9` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AF290  48 8B C4                        mov rax, rsp
006AF293  FA                              cli
006AF294  48 83 EC 10                     sub rsp, 0x10
006AF298  50                              push rax
006AF299  9C                              pushfq
006AF29A  6A 10                           push 0x10
006AF29C  48 8D 05 BD 41 00 00            lea rax, [rip + 0x41bd]
006AF2A3  50                              push rax
006AF2A4  B8 0E 01 00 00                  mov eax, 0x10e
006AF2A9  E9 12 57 01 00                  jmp 0x1406c49c0
006AF2AE  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwLoadDriver(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwLoadDriver(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AF290&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AF290[BB_006AF290]
  bb_006AF2AE[BB_006AF2AE]
```
