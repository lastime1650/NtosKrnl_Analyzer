# sub_00201F78

- RVA: `0x00201F78`–`0x00201F99` (길이 `33` bytes)
- VA: `0x0000000140201F78`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C8BC`
- 디코드: `10`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00201F78  40 88 73 0D                     mov byte ptr [rbx + 0xd], sil
00201F7C  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00201F81  40 80 FE 04                     cmp sil, 4
00201F85  B8 1A 00 00 80                  mov eax, 0x8000001a
00201F8A  0F 45 C5                        cmovne eax, ebp
00201F8D  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
00201F92  48 83 C4 20                     add rsp, 0x20
00201F96  5E                              pop rsi
00201F97  C3                              ret
00201F98  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00201F78(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_rsp;

    *(unsigned __int8 *)(v_rbx + 13) = (unsigned __int8)(v_rsi);
    result = (unsigned int)(0x8000001AULL);
    if (((unsigned __int8)(v_rsi)) != 4) { result = (unsigned int)(v_rbp); }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00201F78(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, int64_t Arg8, int64_t Arg9)
{
    int64_t result;
    int64_t local_rsp;

    *(uint8_t *)(local_rbx + 0xD) = (uint8_t)(local_rsi);
    result = (uint32_t)(0x8000001AULL);
    if (((uint8_t)(local_rsi)) != 4) { result = (uint32_t)(local_rbp); }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00201F78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00201F78[BB_00201F78]
  bb_00201F98[BB_00201F98]
```
