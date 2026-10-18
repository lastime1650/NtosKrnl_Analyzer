# RtlOwnerAcesPresent

- RVA: `0x003FDA10`–`0x003FDA2D` (길이 `29` bytes)
- VA: `0x00000001403FDA10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00099ACC`
- 디코드: `6`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SepAccessCheckAndAuditAlarm](../../page/A1/SepAccessCheckAndAuditAlarm_function_00A1AF4C.md) at `0x00A1BC71`

### Static image references
- `0x003FDA16` → RVA `0x00FD9AA0` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x003FDA27` → [sub_003FDAD6](Unknown_function_003FDAD6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003FDA10  40 55                           push rbp
003FDA12  48 83 EC 20                     sub rsp, 0x20
003FDA16  48 8B 05 83 C0 BD 00            mov rax, qword ptr [rip + 0xbdc083]
003FDA1D  48 8B A8 00 02 00 00            mov rbp, qword ptr [rax + 0x200]
003FDA24  48 85 C9                        test rcx, rcx
003FDA27  0F 84 A9 00 00 00               je 0x1403fdad6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlOwnerAcesPresent(__int64 a1)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
}
```

## 5. (Beta) C Style

```c
int64_t RtlOwnerAcesPresent(int64_t Arg1)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003FDA10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003FDA10[BB_003FDA10]
```
