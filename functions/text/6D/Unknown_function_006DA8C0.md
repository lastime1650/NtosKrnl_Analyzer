# sub_006DA8C0

- RVA: `0x006DA8C0`–`0x006DA8DA` (길이 `26` bytes)
- VA: `0x00000001406DA8C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00067CC4`
- 디코드: `6`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006DA8C4` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006DA8CF` → [FsRtlAcquireFileForModWriteEx + 0x320](../29/FsRtlAcquireFileForModWriteEx_function_00299E5C.md) (`tail-transfer`)
  - `0x006DA8D5` → [FsRtlAcquireFileForModWriteEx + 0x2CC](../29/FsRtlAcquireFileForModWriteEx_function_00299E5C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006DA8C0  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006DA8C4  E8 47 51 B8 FF                  call 0x14025fa10
006DA8C9  45 33 C0                        xor r8d, r8d
006DA8CC  48 85 DB                        test rbx, rbx
006DA8CF  0F 85 A7 F8 BB FF               jne 0x14029a17c
006DA8D5  E9 4E F8 BB FF                  jmp 0x14029a128
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006DA8C0(__int64 a1, __int64 a2, int a3)
{
    __int64 result;

    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_rdi + 8), a2, a3, a4);
    a3 = 0;
}
```

## 5. (Beta) C Style

```c
int64_t sub_006DA8C0(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;

    result = ExReleaseResourceLite(*(uint64_t *)(local_rdi + 0x8), Arg2, Arg3, a4);
    Arg3 = 0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006DA8C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006DA8C0[BB_006DA8C0]
  bb_006DA8D5[BB_006DA8D5]
  bb_006DA8C0 -->|fallthrough| bb_006DA8D5
```
